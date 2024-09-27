import type { IArticle } from "./Article";

export interface ICategory {
  id: number;
  name: string;
}


export interface ICategoryWithArticle extends ICategory {
  id: number;
  name: string;
  allArticles: IArticle[];
}
