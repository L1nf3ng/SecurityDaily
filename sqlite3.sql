PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for authors
-- ----------------------------
DROP TABLE IF EXISTS "authors";
CREATE TABLE "authors" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" TEXT(255) NOT NULL,
  "link" TEXT(255) NOT NULL,
  "create_time" TEXT(60) NOT NULL,
  "extra" blob(255)
);

-- ----------------------------
-- Auto increment value for authors
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 1 WHERE name = 'authors';


-- ----------------------------
-- Table structure for posts
-- ----------------------------
DROP TABLE IF EXISTS "posts";
CREATE TABLE "posts" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "title" TEXT(255) NOT NULL,
  "link" TEXT(255) NOT NULL,
  "tag" TEXT(60),
  "datetime" TEXT(60) NOT NULL,
  "origin" TEXT(60) NOT NULL,
  "author_id" INTEGER(11) NOT NULL,
  "summary" text COMMENT '文章摘要，由ai帮忙总结，字数在200~300左右'
  "extra" blob(255),
  FOREIGN KEY ("author_id") REFERENCES "authors" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);


PRAGMA foreign_keys = true;
