import { Calendar, Clock, User } from "lucide-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

const blogPosts = [
  {
    id: 1,
    title: "The Future of Online Learning",
    excerpt: "Exploring how technology is reshaping education and creating new opportunities for learners worldwide.",
    author: "Sarah Johnson",
    date: "2024-01-15",
    readTime: "5 min read",
    category: "Education",
    image: "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=400&h=250&fit=crop"
  },
  {
    id: 2,
    title: "Career Tips for Tech Professionals",
    excerpt: "Essential strategies for advancing your career in the rapidly evolving technology industry.",
    author: "Mike Chen",
    date: "2024-01-12",
    readTime: "7 min read",
    category: "Career",
    image: "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=400&h=250&fit=crop"
  },
  {
    id: 3,
    title: "Building a Learning Community",
    excerpt: "How forums and discussions enhance the learning experience and create lasting connections.",
    author: "Emma Davis",
    date: "2024-01-10",
    readTime: "4 min read",
    category: "Community",
    image: "https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=400&h=250&fit=crop"
  },
];

export default function Blog() {
  return (
    <div className="copy-protection">
      <div className="bg-gradient-hero text-white py-16">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl text-center">
            <h1 className="text-4xl font-bold tracking-tight sm:text-6xl">
              Blog & Articles
            </h1>
            <p className="mt-6 text-lg leading-8 text-primary-foreground/80">
              Insights, tips, and stories from the world of education and technology
            </p>
          </div>
        </div>
      </div>

      <div className="mx-auto max-w-7xl px-6 py-16 lg:px-8">
        <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
          {blogPosts.map((post) => (
            <Card key={post.id} className="card-hover overflow-hidden">
              <div className="aspect-video overflow-hidden">
                <img
                  src={post.image}
                  alt={post.title}
                  className="h-full w-full object-cover transition-smooth hover:scale-105"
                />
              </div>
              <CardHeader>
                <div className="flex items-center justify-between mb-2">
                  <Badge variant="secondary">{post.category}</Badge>
                  <div className="flex items-center text-sm text-muted-foreground">
                    <Clock className="h-4 w-4 mr-1" />
                    {post.readTime}
                  </div>
                </div>
                <CardTitle className="text-xl hover:text-primary transition-smooth cursor-pointer">
                  {post.title}
                </CardTitle>
                <CardDescription>{post.excerpt}</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="flex items-center justify-between text-sm text-muted-foreground">
                  <div className="flex items-center">
                    <User className="h-4 w-4 mr-1" />
                    {post.author}
                  </div>
                  <div className="flex items-center">
                    <Calendar className="h-4 w-4 mr-1" />
                    {new Date(post.date).toLocaleDateString()}
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </div>
  );
}