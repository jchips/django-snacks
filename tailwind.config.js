/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html',
    './static/src/**/*.js',
    './node_modules/flowbite/**/*.js',
  ],
  darkMode: "media",
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}