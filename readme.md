## Getting Started

1. Build a virtualenv.

2. Migrate:
`python manage.py migrate`
`python manage.py migrate blog`

## Front End

Webpack is installed in `/static`. `cd` into `/static`, to view and edit files. To bundle, type `npm run bundle`. Assets will be placed into a `/dist` directory, and in the root Django directory, run `python manage.py collectstatic`. That'll place all assets in an `/assets` directory in root.

## TODO

Move front end build processes to root so `index.html` can be used via `npm start` -- therefore allowing auto-reloading, etc.
