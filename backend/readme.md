# Run backend

```bash
npx tsc && node dist/index.js
```


## Minify
```bash
npx uglify-js --compress --mangle --output dist/index.min.js -- dist/index.js
```

## Development

```bash
nodemon index.ts
```