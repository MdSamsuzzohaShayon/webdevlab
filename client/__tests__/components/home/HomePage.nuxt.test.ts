import { mount, VueWrapper } from '@vue/test-utils';
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import HomePage from '~/components/home/HomePage.vue';
// import { useAsyncQuery } from '@vue/apollo-composable';
import { ref } from 'vue';
import type { IArticle } from '@/types/Article'; // Assuming IArticle type exists
import { shortDesc } from '~/utils/textFormat';


// Mock utility functions
vi.mock('@/utils', () => ({
  formatReadableDate: vi.fn((date: string) => `Formatted: ${date}`),
  formatRelativeDate: vi.fn((date: string) => `Relative: ${date}`),
  shortDesc: vi.fn((text: string, length: number) => text.substring(0, length))
}));

// Mock the GraphQL query function
vi.mock('@vue/apollo-composable', () => ({
  useAsyncQuery: vi.fn(() => ({
    data: ref({
      value: {
        allArticles: [
          { id: 1, title: 'First Article', thumbnail: 'thumbnail1.jpg', content: 'Content of first article', createdAt: '2024-05-20' },
          { id: 2, title: 'Second Article', thumbnail: 'thumbnail2.jpg', content: 'Content of second article', createdAt: '2024-05-19' }
        ]
      }
    }),
    error: ref(null)
  }))
}));

describe('HomePage Component', () => {
  let wrapper: VueWrapper<any>;

  beforeEach(() => {
    wrapper = mount(HomePage);
  });

  afterEach(() => {
    wrapper.unmount();
  });

  it('should render the component correctly', () => {
    expect(wrapper.exists()).toBe(true);
  });

  it('should fetch and render articles correctly if data exists', async () => {
    await wrapper.vm.$nextTick(); // Wait for the component to finish rendering

    expect(() => {
      const articles: IArticle[] | undefined = wrapper.vm.articles;
      if (!articles) {
        throw new Error('Articles data is undefined');
      }

      expect(articles.length).toBe(2);

      // Check if the first article is rendered correctly
      const firstArticleCard = wrapper.find('.col-md-8 .card');
      expect(firstArticleCard.exists()).toBe(true);
      expect(firstArticleCard.find('h5').text()).toBe(articles[1].title);
      expect(firstArticleCard.find('p').text()).toContain(shortDesc(articles[1].content, 200));
      expect(firstArticleCard.find('small').text()).toBe(`Formatted: ${articles[1].createdAt}`);
    }).not.toThrow();
  });

  /*
  it('should handle errors correctly', async () => {
    vi.mock('@vue/apollo-composable', () => ({
      useAsyncQuery: vi.fn(() => ({
        data: ref(null),
        error: ref('Error fetching articles')
      }))
    }));

    wrapper = mount(HomePage);
    await wrapper.vm.$nextTick(); // Wait for the component to finish rendering

    expect(wrapper.vm.articles).toBeUndefined();
    expect(wrapper.text()).toContain('Error fetching articles');
  });
  */
});
