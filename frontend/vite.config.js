import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

const backend = "http://127.0.0.1:8000";

const rootRedirect = {
  name: "root-redirect",
  configureServer(server) {
    server.middlewares.use((req, res, next) => {
      if (req.url && /^\/static\/app\/?(\?.*)?$/.test(req.url)) {
        res.statusCode = 302;
        res.setHeader("Location", "/");
        res.end();
        return;
      }
      next();
    });
  },
};

export default defineConfig(({ command }) => ({
  plugins: [react(), rootRedirect],
  base: command === "build" ? "/static/app/" : "/",
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
    open: "/",
    proxy: {
      "^/.*[?&]format=json": backend,
      "/static/img": backend,
    },
  },
}));
