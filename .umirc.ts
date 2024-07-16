import { defineConfig } from "umi";

export default defineConfig({
  publicPath: "/static/",
  routes: [
    { path: "/", component: "articles" }
  ],
  npmClient: 'yarn',
});
