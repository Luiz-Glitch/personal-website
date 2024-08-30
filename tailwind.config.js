/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      './templates/**/*.html',
      './static/**/*.css',
    ],
    theme: {
      extend: {
        fontFamily: {
          lora: ['Lora', 'serif'],
        },
      },
    },
    plugins: [],
  }
  