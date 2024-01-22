import { type IAuthor } from "./Author";
import type { ICategory } from "./Category";

export interface IArticle {
  id: number;
  title: string;
  content: string;
  link: string;
  thumbnail: string;
  createdAt?: string;
  category: ICategory;
  author: IAuthor;
}

export interface IArticleProps {
  first: boolean;
  article: IArticle;
}
