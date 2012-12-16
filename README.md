# Mobile HitchHiker Backend

This is a backend for [MobileHitchHiker][1] application.

## Dependencies

```pip install flask```

## Bootstraping

```bash
sqlite3 hitch.db < model.sql # create db and tables
sqlite3 hitch.db < bootstrap.sql # populates with sample data
```

## Running

```
python httpd.py
```

## Example

```
curl -H "Content-Type: application/json" -d @sample_trip.json http://localhost:5000/trips
```

[1]: https://github.com/laurita/MobileHitchHiker
