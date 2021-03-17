
Usage:

```sh
python bs.py <item-file> <payer-1-percent>
```

Example:
```sh
python bs.py items.txt .45
```

---

Build with Docker:

```sh
docker build -t bill-share .
```

Run with Docker:

```sh
docker run -v $PWD/<item-file>:/app/items.txt --rm -it bill-share .45
```
