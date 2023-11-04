import * as React from "react";
import type { HeadFC, PageProps } from "gatsby";
import Layout from "../components/Layout";



const IndexPage: React.FC<PageProps> = () => {
  return (
    <Layout >
      <section className="px-5 py-10 dark:bg-gray-800 dark:text-gray-100">
        <div className="container grid grid-cols-12 mx-auto gap-y-6 md:gap-10">
          <div className="flex flex-col justify-between col-span-12 py-2 space-y-8 md:space-y-16 md:col-span-3">
            <div className="flex flex-col space-y-8 md:space-y-12">
              <div className="flex flex-col space-y-2">
                <h3 className="flex items-center space-x-2 dark:text-gray-400">
                  <span className="flex-shrink-0 w-2 h-2 uppercase rounded-full dark:bg-violet-400"></span>
                  <span className="text-xs font-bold tracki uppercase">Exclusive</span>
                </h3>
                <a rel="noopener noreferrer" href="#" className="font-serif hover:underline">Donec sed elit quis odio mollis dignissim eget et nulla.</a>
                <p className="text-xs dark:text-gray-400">47 minutes ago by
                  <a rel="noopener noreferrer" href="#" className="hover:underline dark:text-violet-400">Leroy Jenkins</a>
                </p>
              </div>
              <div className="flex flex-col space-y-2">
                <h3 className="flex items-center space-x-2 dark:text-gray-400">
                  <span className="flex-shrink-0 w-2 h-2 uppercase rounded-full dark:bg-violet-400"></span>
                  <span className="text-xs font-bold tracki uppercase">Exclusive</span>
                </h3>
                <a rel="noopener noreferrer" href="#" className="font-serif hover:underline">Ut fermentum nunc quis ipsum laoreet condimentum.</a>
                <p className="text-xs dark:text-gray-400">2 hours ago by
                  <a rel="noopener noreferrer" href="#" className="hover:underline dark:text-violet-400">Leroy Jenkins</a>
                </p>
              </div>
              <div className="flex flex-col space-y-2">
                <h3 className="flex items-center space-x-2 dark:text-gray-400">
                  <span className="flex-shrink-0 w-2 h-2 uppercase rounded-full dark:bg-violet-400"></span>
                  <span className="text-xs font-bold tracki uppercase">Exclusive</span>
                </h3>
                <a rel="noopener noreferrer" href="#" className="font-serif hover:underline">Nunc nec ipsum lobortis, pulvinar neque sed.</a>
                <p className="text-xs dark:text-gray-400">4 hours ago by
                  <a rel="noopener noreferrer" href="#" className="hover:underline dark:text-violet-400">Leroy Jenkins</a>
                </p>
              </div>
            </div>
            <div className="flex flex-col w-full space-y-2">
              <div className="flex w-full h-1 bg-opacity-10 dark:bg-violet-400">
                <div className="w-1/2 h-full dark:bg-violet-400"></div>
              </div>
              <a rel="noopener noreferrer" href="#" className="flex items-center justify-between w-full">
                <span className="text-xs font-bold tracki uppercase">See more exclusives</span>
                <svg viewBox="0 0 24 24" strokeWidth="2.5" fill="none" strokeLinecap="round" strokeLinejoin="round" className="w-4 strokeCurrent dark:text-violet-400">
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                  <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
              </a>
            </div>
          </div>
          <div className="relative flex col-span-12 bg-center bg-no-repeat bg-cover dark:bg-gray-500 xl:col-span-6 lg:col-span-5 md:col-span-9 min-h-96" style={{ backgroundImage: 'url("https://source.unsplash.com/random/239x319")' }}>
            <span className="absolute px-1 pb-2 text-xs font-bold uppercase border-b-2 left-6 top-6 dark:border-violet-400 dark:text-gray-100">paris, france</span>
            <a className="flex flex-col items-center justify-end p-6 text-center sm:p-8 group dark:via-transparent flex-grow-1 bg-gradient-to-b dark:from-gray-900 dark:to-gray-900">
              <span className="flex items-center mb-4 space-x-2 dark:text-violet-400">
                <span className="relative flex-shrink-0 w-2 h-2 rounded-full dark:bg-violet-400">
                  <span className="absolute flex-shrink-0 w-3 h-3 rounded-full -left-1 -top-1 animate-ping dark:bg-violet-400"></span>
                </span>
                <span className="text-sm font-bold">Live</span>
              </span>
              <h1 rel="noopener noreferrer" className="font-serif text-2xl font-semibold group-hover:underline dark:text-gray-100">Morbi mattis justo est, ac consectetur dui eleifend vitae. Donec venenatis?</h1>
            </a>
          </div>
          <div className="hidden py-2 xl:col-span-3 lg:col-span-4 md:hidden lg:block">
            <div className="mb-8 space-x-5 border-b-2 border-opacity-10 dark:border-violet-400">
              <button type="button" className="pb-5 text-xs font-bold uppercase border-b-2 dark:border-violet-400">Latest</button>
              <button type="button" className="pb-5 text-xs font-bold uppercase border-b-2 dark:border-transparent dark:text-gray-400">Popular</button>
            </div>
            <div className="flex flex-col divide-y divide-gray-700">
              <div className="flex px-1 py-4">
                <img alt="" className="flex-shrink-0 object-cover w-20 h-20 mr-4 dark:bg-gray-500" src="https://source.unsplash.com/random/244x324" />
                <div className="flex flex-col flex-grow">
                  <a rel="noopener noreferrer" href="#" className="font-serif hover:underline">Aenean ac tristique lorem, ut mollis dui.</a>
                  <p className="mt-auto text-xs dark:text-gray-400">5 minutes ago
                    <a rel="noopener noreferrer" href="#" className="block dark:text-blue-400 lg:ml-2 lg:inline hover:underline">Politics</a>
                  </p>
                </div>
              </div>
              <div className="flex px-1 py-4">
                <img alt="" className="flex-shrink-0 object-cover w-20 h-20 mr-4 dark:bg-gray-500" src="https://source.unsplash.com/random/245x325" />
                <div className="flex flex-col flex-grow">
                  <a rel="noopener noreferrer" href="#" className="font-serif hover:underline">Nulla consectetur efficitur.</a>
                  <p className="mt-auto text-xs dark:text-gray-400">14 minutes ago
                    <a rel="noopener noreferrer" href="#" className="block dark:text-blue-400 lg:ml-2 lg:inline hover:underline">Sports</a>
                  </p>
                </div>
              </div>
              <div className="flex px-1 py-4">
                <img alt="" className="flex-shrink-0 object-cover w-20 h-20 mr-4 dark:bg-gray-500" src="https://source.unsplash.com/random/246x326" />
                <div className="flex flex-col flex-grow">
                  <a rel="noopener noreferrer" href="#" className="font-serif hover:underline">Vitae semper augue purus tincidunt libero.</a>
                  <p className="mt-auto text-xs dark:text-gray-400">22 minutes ago
                    <a rel="noopener noreferrer" href="#" className="block dark:text-blue-400 lg:ml-2 lg:inline hover:underline">World</a>
                  </p>
                </div>
              </div>
              <div className="flex px-1 py-4">
                <img alt="" className="flex-shrink-0 object-cover w-20 h-20 mr-4 dark:bg-gray-500" src="https://source.unsplash.com/random/247x327" />
                <div className="flex flex-col flex-grow">
                  <a rel="noopener noreferrer" href="#" className="font-serif hover:underline">Suspendisse potenti.</a>
                  <p className="mt-auto text-xs dark:text-gray-400">37 minutes ago
                    <a rel="noopener noreferrer" href="#" className="block dark:text-blue-400 lg:ml-2 lg:inline hover:underline">Business</a>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>


      <section className="dark:bg-gray-800 dark:text-gray-100">
        <div className="container max-w-6xl p-6 mx-auto space-y-6 sm:space-y-12">
          <a rel="noopener noreferrer" href="#" className="block max-w-sm gap-3 mx-auto sm:max-w-full group hover:no-underline focus:no-underline lg:grid lg:grid-cols-12 dark:bg-gray-900">
            <img src="https://source.unsplash.com/random/480x360" alt="" className="object-cover w-full h-64 rounded sm:h-96 lg:col-span-7 dark:bg-gray-500" />
            <div className="p-6 space-y-2 lg:col-span-5">
              <h3 className="text-2xl font-semibold sm:text-4xl group-hover:underline group-focus:underline">Noster tincidunt reprimique ad pro</h3>
              <span className="text-xs dark:text-gray-400">February 19, 2021</span>
              <p>Ei delenit sensibus liberavisse pri. Quod suscipit no nam. Est in graece fuisset, eos affert putent doctus id.</p>
            </div>
          </a>
          <div className="grid justify-center grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
            <a rel="noopener noreferrer" href="#" className="max-w-sm mx-auto group hover:no-underline focus:no-underline dark:bg-gray-900">
              <img role="presentation" className="object-cover w-full rounded h-44 dark:bg-gray-500" src="https://source.unsplash.com/random/480x360?1" />
              <div className="p-6 space-y-2">
                <h3 className="text-2xl font-semibold group-hover:underline group-focus:underline">In usu laoreet repudiare legendos</h3>
                <span className="text-xs dark:text-gray-400">January 21, 2021</span>
                <p>Mei ex aliquid eleifend forensibus, quo ad dicta apeirian neglegentur, ex has tantas percipit perfecto. At per tempor albucius perfecto, ei probatus consulatu patrioque mea, ei vocent delicata indoctum pri.</p>
              </div>
            </a>
            <a rel="noopener noreferrer" href="#" className="max-w-sm mx-auto group hover:no-underline focus:no-underline dark:bg-gray-900">
              <img role="presentation" className="object-cover w-full rounded h-44 dark:bg-gray-500" src="https://source.unsplash.com/random/480x360?2" />
              <div className="p-6 space-y-2">
                <h3 className="text-2xl font-semibold group-hover:underline group-focus:underline">In usu laoreet repudiare legendos</h3>
                <span className="text-xs dark:text-gray-400">January 22, 2021</span>
                <p>Mei ex aliquid eleifend forensibus, quo ad dicta apeirian neglegentur, ex has tantas percipit perfecto. At per tempor albucius perfecto, ei probatus consulatu patrioque mea, ei vocent delicata indoctum pri.</p>
              </div>
            </a>
            <a rel="noopener noreferrer" href="#" className="max-w-sm mx-auto group hover:no-underline focus:no-underline dark:bg-gray-900">
              <img role="presentation" className="object-cover w-full rounded h-44 dark:bg-gray-500" src="https://source.unsplash.com/random/480x360?3" />
              <div className="p-6 space-y-2">
                <h3 className="text-2xl font-semibold group-hover:underline group-focus:underline">In usu laoreet repudiare legendos</h3>
                <span className="text-xs dark:text-gray-400">January 23, 2021</span>
                <p>Mei ex aliquid eleifend forensibus, quo ad dicta apeirian neglegentur, ex has tantas percipit perfecto. At per tempor albucius perfecto, ei probatus consulatu patrioque mea, ei vocent delicata indoctum pri.</p>
              </div>
            </a>
            <a rel="noopener noreferrer" href="#" className="max-w-sm mx-auto group hover:no-underline focus:no-underline dark:bg-gray-900 hidden sm:block">
              <img role="presentation" className="object-cover w-full rounded h-44 dark:bg-gray-500" src="https://source.unsplash.com/random/480x360?4" />
              <div className="p-6 space-y-2">
                <h3 className="text-2xl font-semibold group-hover:underline group-focus:underline">In usu laoreet repudiare legendos</h3>
                <span className="text-xs dark:text-gray-400">January 24, 2021</span>
                <p>Mei ex aliquid eleifend forensibus, quo ad dicta apeirian neglegentur, ex has tantas percipit perfecto. At per tempor albucius perfecto, ei probatus consulatu patrioque mea, ei vocent delicata indoctum pri.</p>
              </div>
            </a>
            <a rel="noopener noreferrer" href="#" className="max-w-sm mx-auto group hover:no-underline focus:no-underline dark:bg-gray-900 hidden sm:block">
              <img role="presentation" className="object-cover w-full rounded h-44 dark:bg-gray-500" src="https://source.unsplash.com/random/480x360?5" />
              <div className="p-6 space-y-2">
                <h3 className="text-2xl font-semibold group-hover:underline group-focus:underline">In usu laoreet repudiare legendos</h3>
                <span className="text-xs dark:text-gray-400">January 25, 2021</span>
                <p>Mei ex aliquid eleifend forensibus, quo ad dicta apeirian neglegentur, ex has tantas percipit perfecto. At per tempor albucius perfecto, ei probatus consulatu patrioque mea, ei vocent delicata indoctum pri.</p>
              </div>
            </a>
            <a rel="noopener noreferrer" href="#" className="max-w-sm mx-auto group hover:no-underline focus:no-underline dark:bg-gray-900 hidden sm:block">
              <img role="presentation" className="object-cover w-full rounded h-44 dark:bg-gray-500" src="https://source.unsplash.com/random/480x360?6" />
              <div className="p-6 space-y-2">
                <h3 className="text-2xl font-semibold group-hover:underline group-focus:underline">In usu laoreet repudiare legendos</h3>
                <span className="text-xs dark:text-gray-400">January 26, 2021</span>
                <p>Mei ex aliquid eleifend forensibus, quo ad dicta apeirian neglegentur, ex has tantas percipit perfecto. At per tempor albucius perfecto, ei probatus consulatu patrioque mea, ei vocent delicata indoctum pri.</p>
              </div>
            </a>
          </div>
          <div className="flex justify-center">
            <button type="button" className="px-6 py-3 text-sm rounded-md hover:underline dark:bg-gray-900 dark:text-gray-400">Load more posts...</button>
          </div>
        </div>
      </section>
    </Layout>
  )
}

export default IndexPage

export const Head: HeadFC = () => <title>Home Page</title>
