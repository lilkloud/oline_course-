module.exports = {
  plugins: {
    'postcss-import': {},
    'postcss-nested': {},
    'postcss-preset-env': {
      stage: 1,
      features: {
        'nesting-rules': true,
        'custom-properties': {
          preserve: false,
          importFrom: 'src/styles/variables.css'
        },
        'custom-media-queries': true,
        'color-mod-function': true,
        'custom-selectors': true
      },
      autoprefixer: {
        grid: 'autoplace',
        flexbox: 'no-2009'
      }
    }
  }
};
