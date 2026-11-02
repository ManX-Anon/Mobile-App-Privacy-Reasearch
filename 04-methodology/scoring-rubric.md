# Scoring Rubric: Declared vs. Observed

1. Map each **dangerous** permission to a Play "Data safety" data category using `permission-category-map.csv`.
2. `observed_categories` = set of categories implied by the app's dangerous permissions.
3. `declared_categories` = categories the app lists as collected in Data safety.
4. `undisclosed` = observed - declared.
5. **Score** = number of undisclosed categories (0 = consistent).

| Score | Interpretation |
|-------|----------------|
| 0 | No mismatch found |
| 1-2 | Minor mismatch |
| 3+ | Significant mismatch |

**Caveat:** a permission may be used only on-device (nothing collected). Treat the score as a *flag for further review*, not proof of violation. Add your own justification for the thresholds above.
