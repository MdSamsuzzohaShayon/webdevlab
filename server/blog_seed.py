from core.settings import cloudinary
from graphene.test import Client
from core.schema import schema  # Import your GraphQL schema
from account.models import User
from django.contrib.auth.models import AnonymousUser
from blog.models import Category, Article, Comment, Commenter
from datetime import datetime
from django.db.utils import IntegrityError
import random
from random import randint
from tabulate import tabulate


def cleanup_database():
    # Delete all existing records from relevant tables
    User.objects.all().delete()
    Category.objects.all().delete()
    Article.objects.all().delete()
    Comment.objects.all().delete()
    Commenter.objects.all().delete()

def seed_users():
    # Seed the database with three users
    for i in range(3):
        email = f"user{i+1}@wdl.com"
        password = "password123"
        first_name = f"User{i+1}"
        last_name = "Doe"
        # Assuming birthdate is optional and not required for seeding
        register_mutation = '''
            mutation {
                registerUser(email: "%s", password: "%s", firstName: "%s", lastName: "%s") {
                    user {
                        id
                    }
                }
            }
        ''' % (email, password, first_name, last_name)
        client = Client(schema)
        result = client.execute(register_mutation, context_value={'request': None, 'user': AnonymousUser()})
        print(f"User {i+1} created with ID: {result['data']['registerUser']['user']['id']}")

def verify_users():
    # Verify all the users
    users = User.objects.all()
    for user in users:
        user.is_active = True
        user.save()


def login_and_get_tokens():
    # Log in each user and get their tokens
    for i in range(3):
        email = f"user{i+1}@wdl.com"
        password = "password123"
        login_mutation = '''
            mutation {
                login(email: "%s", password: "%s") {
                    user{
                      id
                      email
                      firstName
                      lastName
                    }
                    accessToken
                    refreshToken
                }
            }
        ''' % (email, password)
        client = Client(schema)
        result = client.execute(login_mutation, context_value={'request': None, 'user': AnonymousUser()})
        access_token = result['data']['login']['accessToken']
        refresh_token = result['data']['login']['refreshToken']
        user = result['data']['login']['user']
        print(f"User {i+1} logged in:")
        print(f"Access Token: {access_token}")
        print(f"Refresh Token: {refresh_token}")
        print(f"User: {user}")



def seed_data():
    # Create and verify users
    users = User.objects.all()[:3]  # Assuming you have at least 3 verified users

    # Create 5 categories (Tech category)
    categories = []
    for i in range(5):
        category = Category.objects.create(name=f"Tech category {i + 1}")
        categories.append(category)

    commenters = []
    for i in range(10):
        commenter = Commenter.objects.create(
            name=f"Commenter {i + 1}",
            email=f"commenter{i + 1}@wdl.com"
        )
        commenters.append(commenter)

    # Upload thumbnail and save public ID for each article
    articles_data = [
        {
            "title": "India’s election overshadowed by the rise of online misinformation",
            "content": "As India kicks off the world’s biggest election, which starts on April 19 and runs through June 1, the electoral landscape is overshadowed by misinformation. The country — which has more than 830 million internet users and is home to the largest user base for social media platforms like Facebook and Instagram — is already at the highest risk of misinformation and disinformation, according to the World Economic Forum. AI has complicated the situation further, including deepfakes created with generative AI. Misinformation is not just a problem for election fairness — it can have deadly effects, including violence on the ground and increase hatred for minorities. Pratik Sinha, the co-founder of the Indian non-profit fact-checking website Alt News, says there’s been an increase in the deliberate creation of misinformation to polarize society. “Ever since social media has been thriving, there is a new trend where you use misinformation to target communities,” he said.",
            "thumbnail": "static/01.webp",
            "category_id": random.choice(categories).id,  # Replace with the actual category ID
            "author_id": random.choice(users).id
        },
        {
            "title": "CesiumAstro claims former exec spilled trade secrets to upstart competitor AnySignal",
            "content": "CesiumAstro alleges in a newly filed lawsuit that a former executive disclosed trade secrets and confidential information about sensitive tech, investors and customers to a competing startup. Austin-based Cesium develops active-phased array and software-defined radio systems for spacecraft, missiles and drones. While phased-array antenna systems have been used on satellites for decades, Cesium has considerably advanced and productized the tech over its seven years in operation. The startup has landed more than $100 million in venture and government funding, which it has used to develop a suite of products for commercial and defense customers.",
            "thumbnail": "static/02.webp",
            "category_id": random.choice(categories).id,  # Replace with the actual category ID
            "author_id": random.choice(users).id
        },
        {
            "title": "Tesla recalls the Cybertruck for faulty accelerator pedals that can get stuck",
            "content": "Tesla is recalling all 3,878 Cybertrucks that it has shipped to date, due to a problem where the accelerator pedal can get stuck, putting drivers at risk of a crash, according to the National Highway Traffic Safety Administration. The recall caps a tumultuous week for Tesla. The company laid off more than 10% of its workforce on Monday, and lost two of its highest-ranking executives. A few days later, Tesla asked shareholders to re-vote on CEO Elon Musk’s massive compensation package that was struck down by a judge earlier this year. Reports of problems with the Cybertruck’s accelerator pedal started popping up in the last few weeks. Tesla even reportedly paused deliveries of the truck while it sorted out the issue. Musk said in a post on X that Tesla was being very cautious and the company reported to NHTSA that it was not aware of any crashes or injuries related to the problem. The company has now confirmed to NHTSA that the pedal can dislodge, making it possible for it to slide up and get caught in the trim around the footwell. Tesla said it first received a notice of one of these accelerator pedal incidents from a customer on March 31, and then a second one on April 3. After performing a series of tests, it decided on April 12 to issue a recall after determining that [a]n unapproved change introduced lubricant (soap) to aid in the component assembly of the pad onto the accelerator pedal,” and that “[r]esidual lubricant reduced the retention of the pad to the pedal.” Tesla says it will replace or rework the accelerator pedal on all existing Cybertrucks. It also told NHTSA that it has started building Cybertrucks with a new accelerator pedal, and that it’s fixing the vehicles that are in transit or sitting at delivery centers. While the Cybertruck only first started shipping late last year, this is not the vehicle’s first recall. But the initial one was minor: Earlier this year, Tesla recalled the software on all of its vehicles because the font sizes of its warning lights were too small. The company unveiled the truck back in 2019.",
            "thumbnail": "static/03.webp",
            "category_id": random.choice(categories).id,  # Replace with the actual category ID
            "author_id": random.choice(users).id
        },
        {
            "title": "Why vector databases are having a moment as the AI hype cycle peaks",
            "content": "Vector databases are all the rage, judging by the number of startups entering the space and the investors ponying up for a piece of the pie. The proliferation of large language models (LLMs) and the generative AI (GenAI) movement have created fertile ground for vector database technologies to flourish.",
            "thumbnail": "static/04.webp",
            "category_id": random.choice(categories).id,  # Replace with the actual category ID
            "author_id": random.choice(users).id
        },
        {
            "title": "Notable Capital’s Hans Tung on the state of VC and the upside to down rounds",
            "content": "To some investors, “down round” is a dirty phrase, but not to Notable Capital’s Hans Tung. Hans is a managing partner at Notable Capital, formerly GGV Capital, a venture firm focusing on investments in the U.S., Latin America, Israel, and Europe. Hans, whose portfolio includes the likes of Airbnb, StockX and Slack, sat down with TechCrunch’s Equity podcast to discuss the overall state of venture and why he still believes down rounds can make a lot of sense. Per Hans, “An IPO is actually just a milestone, not the end game. An IPO is the beginning of public investors being along for the ride. So when you think in longer-term valuations, up or down temporarily doesn’t matter as much as generating a big outcome at the end.” It’s worth noting that by September 2023, nearly 11% of the year’s VC deals were down rounds, according to PitchBook data. Hans also let us know why he’s still bullish on fintech, and what sectors in the fintech space have him especially psyched. Of course, we dug into recent changes at his own firm, which evolved from 24-year-old cross-border firm GGV Capital and rebranded its U.S. and Asia operations to Notable Capital and Granite Asia, respectively. GGV’s transformation is the latest in a string of changes we’ve seen in the world of venture capital, including personnel changes at Founders Fund, Benchmark and Thrive Capital. Hit play to hear what Hans has to say on these topics and more! Equity will be back on Monday. See you then! Equity is TechCrunch’s flagship podcast and posts every Monday, Wednesday and Friday. You can subscribe to us on Apple Podcasts, Overcast, Spotify and all the casts. You also can follow Equity on X and Threads, at @EquityPod. For the full interview transcript, for those who prefer reading over listening, check out our full archive of episodes over at Simplecast.",
            "thumbnail": "static/05.webp",
            "category_id": random.choice(categories).id,  # Replace with the actual category ID
            "author_id": random.choice(users).id
        },
        {
            "title": "This Week in AI: When ‘open source’ isn’t so open",
            "content": "Keeping up with an industry as fast-moving as AI is a tall order. So until an AI can do it for you, here’s a handy roundup of recent stories in the world of machine learning, along with notable research and experiments we didn’t cover on their own. This week, Meta released the latest in its Llama series of generative AI models: Llama 3 8B and Llama 3 70B. Capable of analyzing and writing text, the models are “open sourced, Meta said — intended to be a “foundational piece of systems that developers design with their unique goals in mind. “We believe these are the best open source models of their class, period, Meta wrote in a blog post. “We are embracing the open source ethos of releasing early and often. There’s only one problem: the Llama 3 models aren’t really “open source, at least not in the strictest definition. Open source implies that developers can use the models how they choose, unfettered. But in the case of Llama 3 — as with Llama 2 — Meta has imposed certain licensing restrictions. For example, Llama models can’t be used to train other models. And app developers with over 700 million monthly users must request a special license from Meta.  Debates over the definition of open source aren’t new. But as companies in the AI space play fast and loose with the term, it’s injecting fuel into long-running philosophical arguments. Last August, a study co-authored by researchers at Carnegie Mellon, the AI Now Institute and the Signal Foundation found that many AI models branded as “open source come with big catches — not just Llama. The data required to train the models is kept secret. The compute power needed to run them is beyond the reach of many developers. And the labor to fine-tune them is prohibitively expensive. So if these models aren’t truly open source, what are they, exactly? That’s a good question; defining open source with respect to AI isn’t an easy task. One pertinent unresolved question is whether copyright, the foundational IP mechanism open source licensing is based on, can be applied to the various components and pieces of an AI project, in particular a model’s inner scaffolding (e.g. embeddings). Then, there’s the mismatch between the perception of open source and how AI actually functions to overcome: open source was devised in part to ensure that developers could study and modify code without restrictions. With AI, though, which ingredients you need to do the studying and modifying is open to interpretation. Wading through all the uncertainty, the Carnegie Mellon study does make clear the harm inherent in tech giants like Meta co-opting the phrase “open source. Often, “open source AI projects like Llama end up kicking off news cycles — free marketing — and providing technical and strategic benefits to the projects’ maintainers. The open source community rarely sees these same benefits, and, when they do, they’re marginal compared to the maintainers’. Instead of democratizing AI, “open source AI projects — especially those from big tech companies — tend to entrench and expand centralized power, say the study’s co-authors. That’s good to keep in mind the next time a major “open source model release comes around. Here are some other AI stories of note from the past few days: Meta updates its chatbot: Coinciding with the Llama 3 debut, Meta upgraded its AI chatbot across Facebook, Messenger, Instagram and WhatsApp — Meta AI — with a Llama 3-powered backend. It also launched new features, including faster image generation and access to web search results. AI-generated porn: Ivan writes about how the Oversight Board, Meta’s semi-independent policy council, is turning its attention to how the company’s social platforms are handling explicit, AI-generated images. Snap watermarks: Social media service Snap plans to add watermarks to AI-generated images on its platform. A translucent version of the Snap logo with a sparkle emoji, the new watermark will be added to any AI-generated image exported from the app or saved to the camera roll. The new Atlas: Hyundai-owned robotics company Boston Dynamics has unveiled its next-generation humanoid Atlas robot, which, in contrast to its hydraulics-powered predecessor, is all-electric — and much friendlier in appearance. Humanoids on humanoids: Not to be outdone by Boston Dynamics, the founder of Mobileye, Amnon Shashua, has launched a new startup, Menteebot, focused on building bibedal robotics systems. A demo video shows Menteebot’s prototype walking over to a table and picking up fruit. Reddit, translated: In an interview with Amanda, Reddit CPO Pali Bhat revealed that an AI-powered language translation feature to bring the social network to a more global audience is in the works, along with an assistive moderation tool trained on Reddit moderators’ past decisions and actions. AI-generated LinkedIn content: LinkedIn has quietly started testing a new way to boost its revenues: a LinkedIn Premium Company Page subscription, which — for fees that appear to be as steep as $99/month — include AI to write content and a suite of tools to grow follower counts. A Bellwether: Google parent Alphabet’s moonshot factory, X, this week unveiled Project Bellwether, its latest bid to apply tech to some of the world’s biggest problems. Here, that means using AI tools to identify natural disasters like wildfires and flooding as quickly as possible. Protecting kids with AI: Ofcom, the regulator charged with enforcing the U.K.’s Online Safety Act, plans to launch an exploration into how AI and other automated tools can be used to proactively detect and remove illegal content online, specifically to shield children from harmful content. OpenAI lands in Japan: OpenAI is expanding to Japan, with the opening of a new Tokyo office and plans for a GPT-4 model optimized specifically for the Japanese language. More machine learnings Human And Artificial Intelligence Cooperating Concept Can a chatbot change your mind? Swiss researchers found that not only can they, but if they are pre-armed with some personal information about you, they can actually be more persuasive in a debate than a human with that same info. This is Cambridge Analytica on steroids, said project lead Robert West from EPFL. The researchers suspect the model — GPT-4 in this case — drew from its vast stores of arguments and facts online to present a more compelling and confident case. But the outcome kind of speaks for itself. Don’t underestimate the power of LLMs in matters of persuasion, West warned: “In the context of the upcoming US elections, people are concerned because that’s where this kind of technology is always first battle tested. One thing we know for sure is that people will be using the power of large language models to try to swing the election. Why are these models so good at language anyway? That’s one area there is a long history of research into, going back to ELIZA. If you’re curious about one of the people who’s been there for a lot of it (and performed no small amount of it himself), check out this profile on Stanford’s Christopher Manning. He was just awarded the John von Neuman Medal; congrats! In a provocatively titled interview, another long-term AI researcher (who has graced the TechCrunch stage as well), Stuart Russell, and postdoc Michael Cohen speculate on “How to keep AI from killing us all. Probably a good thing to figure out sooner rather than later! It’s not a superficial discussion, though — these are smart people talking about how we can actually understand the motivations (if that’s the right word) of AI models and how regulations ought to be built around them. The interview is actually regarding a paper in Science published earlier this month, in which they propose that advanced AIs capable of acting strategically to achieve their goals, which they call  “long-term planning agents, may be impossible to test. Essentially, if a model learns to “understand the testing it must pass in order to succeed, it may very well learn ways to creatively negate or circumvent that testing. We’ve seen it at a small scale, why not a large one? Russell proposes restricting the hardware needed to make such agents… but of course, Los Alamos and Sandia National Labs just got their deliveries. LANL just had the ribbon-cutting ceremony for Venado, a new supercomputer intended for AI research, composed of 2,560 Grace Hopper Nvidia chips. Researchers look into the new neuromorphic computer. And Sandia just received “an extraordinary brain-based computing system called Hala Point, with 1.15 billion artificial neurons, built by Intel and believed to be the largest such system in the world. Neuromorphic computing, as it’s called, isn’t intended to replace systems like Venado, but to pursue new methods of computation that are more brain-like than the rather statistics-focused approach we see in modern models. With this billion-neuron system, we will have an opportunity to innovate at scale both new AI algorithms that may be more efficient and smarter than existing algorithms, and new brain-like approaches to existing computer algorithms such as optimization and modeling, said Sandia researcher Brad Aimone. Sounds dandy… just dandy!",
            "thumbnail": "static/06.webp",
            "category_id": random.choice(categories).id,  # Replace with the actual category ID
            "author_id": random.choice(users).id
        },
        {
            "title": "Lawmakers vote to reauthorize US spying law that critics say expands government surveillance",
            "content": "Lawmakers passed legislation early Saturday reauthorizing and expanding a controversial U.S. surveillance law shortly after the powers expired at midnight, rejecting opposition by privacy advocates and lawmakers.",
            "thumbnail": "static/07.webp",
            "category_id": random.choice(categories).id,  # Replace with the actual category ID
            "author_id": random.choice(users).id
        },
        {
            "title": "Women in AI: Allison Cohen on building responsible AI projects",
            "content": "To give AI-focused women academics and others their well-deserved — and overdue — time in the spotlight, TechCrunch has been publishing a series of interviews focused on remarkable women who’ve contributed to the AI revolution.",
            "thumbnail": "static/08.webp",
            "category_id": random.choice(categories).id,  # Replace with the actual category ID
            "author_id": random.choice(users).id
        },
        {
            "title": "Your Android phone could have stalkerware — here’s how to remove it",
            "content": "Consumer-grade spyware apps that covertly and continually monitor your private messages, photos, phone calls and real-time location are a growing problem for Android users.",
            "thumbnail": "static/09.webp",
            "category_id": random.choice(categories).id,  # Replace with the actual category ID
            "author_id": random.choice(users).id
        },
        {
            "title": "Too many models",
            "content": "How many AI models is too many? It depends on how you look at it, but 10 a week is probably a bit much. That’s roughly how many we’ve seen roll out in the last few days, and it’s increasingly hard to say whether and how these models compare to one another, if it was ever possible to begin with. So what’s the point?",
            "thumbnail": "static/10.webp",
            "category_id": random.choice(categories).id,  # Replace with the actual category ID
            "author_id": random.choice(users).id
        },
    ]

    for article_data in articles_data:
        try:
            category_id = article_data.pop("category_id")
            author_id = article_data.pop("author_id")
            category = Category.objects.get(pk=category_id)
            author = User.objects.get(pk=author_id)

            # Upload thumbnail to Cloudinary
            thumbnail_path = article_data.pop("thumbnail")
            thumbnail_upload_response = cloudinary.uploader.upload(thumbnail_path)

            # Get the public ID of the uploaded thumbnail
            thumbnail_url = thumbnail_upload_response['public_id']

            # Add thumbnail URL to article data
            article_data["thumbnail"] = thumbnail_url

            article_data["category"] = category
            article_data["author"] = author
            article = Article.objects.create(**article_data)

            # Randomly determine the number of comments for each article
            num_comments = random.randint(0, 5)
            for _ in range(num_comments):
                commenter = random.choice(commenters)
                Comment.objects.create(
                    article=article,
                    commenter=commenter,
                    text="This is a sample comment."
                )

        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            # Handle the integrity error, e.g., log the error or skip the creation of the problematic record
            pass

def display_data():
    # Fetch data from all relevant models
    users = User.objects.all()
    categories = Category.objects.all()
    articles = Article.objects.all()
    comments = Comment.objects.all()

    # Format data into tables
    user_data = [[user.id, user.first_name, user.last_name, user.email] for user in users]
    category_data = [[category.id, category.name] for category in categories]
    article_data = [[
        article.id,
        article.title,
        article.content,
        article.thumbnail,
        article.category.name,
        f"{article.author.first_name} {article.author.last_name}"
    ] for article in articles]
    comment_data = [[comment.id, comment.text, comment.article.title] for comment in comments]

    # Define headers for each table
    user_headers = ["ID", "First Name", "Last Name", "Email"]
    category_headers = ["ID", "Name"]
    article_headers = ["ID", "Title", "Content", "Thumbnail", "Category", "Author"]
    comment_headers = ["ID", "Content", "Article Title"]

    # Display tables
    print("Users:")
    print(tabulate(user_data, headers=user_headers, tablefmt="grid"))
    print("\nCategories:")
    print(tabulate(category_data, headers=category_headers, tablefmt="grid"))
    print("\nArticles:")
    print(tabulate(article_data, headers=article_headers, tablefmt="grid"))
    print("\nComments:")
    print(tabulate(comment_data, headers=comment_headers, tablefmt="grid"))

# Terminal commands
# ./manage.py shell

"""
./manage.py shell
>>> from blog_seed import seed_users, verify_users, login_and_get_tokens, seed_data, cleanup_database
>>> cleanup_database()
>>> seed_users()
>>> verify_users()
>>> login_and_get_tokens()
>>> seed_data()
"""
