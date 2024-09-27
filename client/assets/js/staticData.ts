import type { IMenuItem } from "~/types";

const adminMenuList: IMenuItem[] = [
  { id: 1, iconName: iName.settings, link: '/admin/settings', text: 'settings' },
  { id: 2, iconName: iName.comments, link: '/admin/comments', text: 'Comments' },
  { id: 3, iconName: iName.auther, link: '/admin/author', text: 'Author' },
  {
    id: 4,
    iconName: iName.tags,
    link: '/admin/tags',
    text: 'Tags',
  },
  { id: 5, iconName: iName.category, link: '/admin/category', text: 'Category' },
  { id: 6, iconName: iName.article, link: '/admin/article', text: 'Article' },
];

const userMenuList: IMenuItem[] = [
  { id: 1, iconName: iName.tags, text: 'Home', link: '/' },
  { id: 2, iconName: iName.tags, text: 'Course', link: '/course' },
  { id: 3, iconName: iName.tags, text: 'Blog', link: '/blog' },
  { id: 4, iconName: iName.tags, text: 'Shorts', link: '/shorts' },
  { id: 5, iconName: iName.tags, text: 'Services', link: '/services' },
  { id: 6, iconName: iName.tags, text: 'Contact', link: '/contact' },
  { id: 7, iconName: iName.tags, text: 'About', link: '/about' },
];

export { adminMenuList, userMenuList };
