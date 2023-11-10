import { type IAuthor } from "./Author";
import type { ICategory } from "./Category";

export interface IArticle {
  id: number;
  title: string;
  content: string;
  createdAt: string;
  author: IAuthor;
  category: ICategory;
  link: string;
}

export interface IArticleProps {
  first: boolean;
  article: IArticle;
}
