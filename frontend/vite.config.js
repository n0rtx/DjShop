import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

const backend = "http://127.0.0.1:8000";

export default defineConfig({
  plugins: [react()],
  base: "/static/app/",
  build: {
    outDir: "../backend/static/app",
    emptyOutDir: true,
    cssCodeSplit: false,
    rollupOptions: {
      input: "src/main.jsx",
      output: {
        entryFileNames: "app.js",
        chunkFileNames: "chunks/[name].js",
        assetFileNames: (asset) => (asset.name && asset.name.endsWith(".css") ? "app.css" : "assets/[name][extname]"),
      },
    },
  },
  server: {
    port: 5173,
    proxy: {
      "^/.*[?&]format=json": backend,
      "/static/img": backend,
    },
  },
});
