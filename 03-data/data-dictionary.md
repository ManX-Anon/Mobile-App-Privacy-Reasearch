# Data Dictionary

## processed/permissions.csv
| Column | Meaning |
|--------|---------|
| app_id | ID from app-list.csv |
| package | Android package name |
| permission | Full permission string (e.g., android.permission.CAMERA) |
| status | MobSF/Android protection level: normal, dangerous, signature, unknown |

## processed/trackers.csv
| app_id | tracker_name |

## processed/domains-contacted.csv
| app_id | host | request_count |

## processed/mismatch-scores.csv
| Column | Meaning |
|--------|---------|
| observed_categories | Data categories implied by dangerous permissions (via permission-category-map.csv) |
| declared_categories | Categories declared as collected in the Data safety section |
| undisclosed | Observed but not declared |
| score | Number of undisclosed categories (see scoring-rubric.md) |
