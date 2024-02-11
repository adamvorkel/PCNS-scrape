import fs from "fs";
import express, { Request, Response } from "express";

const htmlHit = fs.readFileSync("./data.html", {
  encoding: "utf-8",
  flag: "r",
});
const htmlMiss = fs.readFileSync("./nodata.html", {
  encoding: "utf-8",
  flag: "r",
});

const waitFor = (ms: number) =>
  new Promise((resolve) => setTimeout(resolve, ms));

const app = express();
const port = 3000;
const delay = 7500;

app.post("/hit", async (req: Request, res: Response) => {
  res.setHeader("Content-Type", "text/html");
  await waitFor(delay);
  res.send(htmlHit);
});

app.post("/miss", async (req: Request, res: Response) => {
  res.setHeader("Content-Type", "text/html");
  await waitFor(delay);
  res.send(htmlMiss);
});

app.listen(port, () => console.log(`Server listening on port ${port}`));
