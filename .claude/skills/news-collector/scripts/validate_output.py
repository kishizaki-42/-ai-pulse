#!/usr/bin/env python3
"""
Validate data/current.json against the NewsData schema.

Usage:
    python scripts/validate_output.py [path/to/current.json]

Default path: data/current.json
"""

import json
import sys
import re
from pathlib import Path
from datetime import datetime

def validate_id(id_str: str) -> bool:
    """Validate ID format: YYYYMMDD-NNN"""
    return bool(re.match(r'^\d{8}-\d{3}$', id_str))

def validate_url(url: str) -> bool:
    """Validate URL format"""
    return url.startswith('http://') or url.startswith('https://')

def validate_iso_date(date_str: str) -> bool:
    """Validate ISO 8601 date format"""
    try:
        datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return True
    except ValueError:
        return False

def validate_article(article: dict, index: int) -> list[str]:
    """Validate a single news article"""
    errors = []
    required = ['id', 'title', 'url', 'sourceName', 'category', 'publishedAt', 'summary', 'importance']

    for field in required:
        if field not in article:
            errors.append(f"Article {index}: missing '{field}'")

    if 'id' in article and not validate_id(article['id']):
        errors.append(f"Article {index}: invalid id format '{article['id']}' (expected YYYYMMDD-NNN)")

    if 'url' in article and not validate_url(article['url']):
        errors.append(f"Article {index}: invalid url '{article['url']}'")

    if 'category' in article and article['category'] not in ['Model', 'Service', 'Other']:
        errors.append(f"Article {index}: invalid category '{article['category']}'")

    if 'importance' in article and article['importance'] not in ['high', 'normal']:
        errors.append(f"Article {index}: invalid importance '{article['importance']}'")

    if 'publishedAt' in article and not validate_iso_date(article['publishedAt']):
        errors.append(f"Article {index}: invalid publishedAt format '{article['publishedAt']}'")

    if 'summary' in article and len(article['summary']) > 200:
        errors.append(f"Article {index}: summary too long ({len(article['summary'])} chars, max 200)")

    return errors

def validate_news_data(data: dict) -> list[str]:
    """Validate the entire NewsData structure"""
    errors = []

    if 'lastUpdated' not in data:
        errors.append("Missing 'lastUpdated'")
    elif not validate_iso_date(data['lastUpdated']):
        errors.append(f"Invalid lastUpdated format: '{data['lastUpdated']}'")

    if 'news' not in data:
        errors.append("Missing 'news' array")
    elif not isinstance(data['news'], list):
        errors.append("'news' must be an array")
    else:
        urls = set()
        for i, article in enumerate(data['news']):
            errors.extend(validate_article(article, i))
            if 'url' in article:
                if article['url'] in urls:
                    errors.append(f"Article {i}: duplicate url '{article['url']}'")
                urls.add(article['url'])

    return errors

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'data/current.json'

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}")
        sys.exit(1)

    errors = validate_news_data(data)

    if errors:
        print(f"Validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        article_count = len(data.get('news', []))
        high_count = sum(1 for a in data.get('news', []) if a.get('importance') == 'high')
        print(f"Validation passed: {article_count} articles ({high_count} high importance)")
        sys.exit(0)

if __name__ == '__main__':
    main()
