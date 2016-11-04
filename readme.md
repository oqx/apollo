## Getting Started

1. Build a virtualenv.

2. Migrate:
`python manage.py migrate`
`python manage.py migrate blog`

## Front End

Webpack & NPM are installed in `/static`. 

1. `cd` into `/static` to view and edit files Type `npm install` to install packages.

2. Bundle by typing `npm run bundle`. Assets will be placed into a `/dist` directory.

3. In the root project directory, run `python manage.py collectstatic`. That'll place all assets in an `/assets` directory in root.

## TODO

Move front end build processes to root so `index.html` can be used via `npm start` -- therefore allowing auto-reloading, etc.
