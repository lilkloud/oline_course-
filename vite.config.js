import { defineConfig } from 'vite';
import { resolve } from 'path';
import basicSsl from '@vitejs/plugin-basic-ssl';
import viteImagemin from 'vite-plugin-imagemin';
import viteCompression from 'vite-plugin-compression';
import { createHtmlPlugin } from 'vite-plugin-html';
import { VitePWA } from 'vite-plugin-pwa';

export default defineConfig(({ mode }) => {
  const isProduction = mode === 'production';
  
  return {
    base: isProduction ? '/static/' : '/',
    publicDir: 'public',
    plugins: [
      basicSsl(),
      createHtmlPlugin({
        minify: isProduction,
        inject: {
          data: {
            title: '9kloud - Online Learning Platform',
            description: 'Learn new skills with our high-quality online courses',
            themeColor: '#6c7bff',
          },
        },
      }),
      VitePWA({
        registerType: 'autoUpdate',
        includeAssets: ['favicon.ico', 'apple-touch-icon.png', 'safari-pinned-tab.svg'],
        manifest: {
          name: '9kloud',
          short_name: '9kloud',
          description: 'Online Learning Platform',
          theme_color: '#6c7bff',
          background_color: '#0b0f17',
          display: 'standalone',
          icons: [
            {
              src: '/static/img/icons/icon-192x192.png',
              sizes: '192x192',
              type: 'image/png',
            },
            {
              src: '/static/img/icons/icon-512x512.png',
              sizes: '512x512',
              type: 'image/png',
            },
          ],
        },
      }),
      viteImagemin({
        gifsicle: { optimizationLevel: 7, interlaced: false },
        optipng: { optimizationLevel: 7 },
        mozjpeg: { quality: 80 },
        pngquant: { quality: [0.8, 0.9], speed: 4 },
        webp: { quality: 80 },
        svgo: {
          plugins: [
            { name: 'removeViewBox', active: false },
            { name: 'cleanupIDs', active: false },
          ],
        },
      }),
      viteCompression({
        algorithm: 'brotliCompress',
        ext: '.br',
        threshold: 1024,
        deleteOriginFile: false,
      }),
    ],
    resolve: {
      alias: {
        '@': resolve(__dirname, './src'),
        '~bootstrap': 'bootstrap',
        '~@fontsource': resolve(__dirname, 'node_modules/@fontsource'),
      },
    },
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: `
            @import "src/styles/_variables.scss";
            @import "src/styles/_mixins.scss";
          `,
        },
      },
      devSourcemap: true,
    },
    server: {
      port: 3000,
      strictPort: true,
      open: false,
      cors: true,
      proxy: {
        '^/(api|admin|media|static)/': {
          target: 'http://localhost:8000',
          changeOrigin: true,
          secure: false,
          ws: true,
        },
      },
    },
    build: {
      outDir: 'dist',
      assetsDir: 'assets',
      emptyOutDir: true,
      sourcemap: isProduction ? false : 'inline',
      manifest: true,
      rollupOptions: {
        input: {
          main: resolve(__dirname, 'src/js/main.js'),
        },
        output: {
          assetFileNames: 'assets/[name]-[hash][extname]',
          chunkFileNames: 'assets/[name]-[hash].js',
          entryFileNames: 'assets/[name]-[hash].js',
          manualChunks: (id) => {
            if (id.includes('node_modules')) {
              if (id.includes('bootstrap') || id.includes('@popperjs')) {
                return 'vendor';
              }
              return 'vendor-other';
            }
          },
        },
      },
      chunkSizeWarningLimit: 1000,
      minify: isProduction ? 'terser' : false,
      terserOptions: {
        compress: {
          drop_console: isProduction,
          drop_debugger: isProduction,
        },
      },
    },
    optimizeDeps: {
      include: ['bootstrap', '@popperjs/core'],
      exclude: [],
    },
  };
});
