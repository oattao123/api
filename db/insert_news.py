import mysql.connector
from datetime import datetime

# Function to parse date from the given format to MySQL format
def parse_date(date_string):
    return datetime.strptime(date_string, '%d %b - %Y').strftime('%Y-%m-%d')

# Data for insertion
news_data = [
    {
        "id": 1,
        "cover": "../images/hero/hero1.jpg",
        "catgeory": "featured",
        "title": "Google To Boost Android Security In Few Days",
        "authorName": "Salman",
        "authorImg": "../images/author.jpg",
        "time": "5 Jun - 2022",
        "desc": [
            {"para1": "You audience. Least, the recently his repeat the this avarice for the have and was on would before the concise bedding were hall politely name be regretting have of even five of it the his are there again. Word seven designer far lady problem will have work with you to fully understand your business to achieve."},
            {"para2": "We work with clients big and small across a range of sectors and we utilize all forms of media to get your name out there in a way that’s right for you. We believe that analysis of your company and your customers is key in responding effectively to your promotional needs and we will work with you."},
            {"para3": "We have a number of different teams within our agency that specialise in different areas of business so you can be sure that you won’t receive a generic service and although we can’t boast years and years of service we can ensure you that is a good thing in this industry."},
        ],
        "details": [
            {"title": "Starting a new company is easy"},
            {"para1": "Our teams are up to date with the latest technologies, media trends and are keen to prove themselves in this industry and that’s what you want from an advertising agency, not someone who is relying on the same way of doing things that worked 10 years, 5 years or even a year ago."},
            {"quote": "Scarfs, still not this no with explains it me and option on the any options roasted when I and state can that an don't subjective of has his take on and in from royal everything took raising our have behind success you the mechanic."},
            {"para2": "And, higher by agency; In from their in and we spirit, through merely and doctor's small him sounded a all now, with that put gift white highly geared that was left back as of or logged important. A over have the large try understanding the believe. Perfected been viewer. Shreds early willingly safely what passion the."},
            {"para3": "In an ideal world this website wouldn’t exist, a client would acknowledge the importance of having web copy before the design starts. Needless to say it’s very important, content is king and people are beginning to understand that. However, back over in reality some project schedules and budgets don’t allow for web copy to be written before the design phase, this is sad but true."},
        ],
    },
    # Add additional news items in the same format
]

# ... rest of your script remains the same


# Establish a connection to the database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@oattao@123",
    database="StockPortfolio_main"
)

# Create a cursor object using the cursor() method
cursor = connection.cursor()

# SQL query for inserting data
add_news = ("INSERT INTO news "
            "(title, author_name, author_image, date_published, short_description, full_content, category, cover_image, related_asset) "
            "VALUES (%(title)s, %(author_name)s, %(author_image)s, %(date_published)s, %(short_description)s, %(full_content)s, %(category)s, %(cover_image)s, %(related_asset)s)")

# Process each news item
for news_item in news_data:
    # Combine all the paragraphs from desc and details into full_content
    full_content = ' '.join(para.get('para1', '') for para in news_item['desc'])
    full_content += ' '.join(para.get('para1', '') for para in news_item.get('details', []))

    # Use the first paragraph from desc as the short description
    short_description = news_item['desc'][0]['para1'] if news_item['desc'] else ''

    # Parse the published date
    date_published = parse_date(news_item['time'])

    # Define the data record to insert
    data_news = {
        'title': news_item['title'],
        'author_name': news_item['authorName'],
        'author_image': news_item['authorImg'],
        'date_published': date_published,
        'short_description': short_description,
        'full_content': full_content,
        'category': news_item['catgeory'],  # Assuming 'catgeory' is a typo, change to 'category' if necessary
        'cover_image': news_item['cover'],
        'related_asset': None  # Placeholder, assuming there is no related_asset data
    }

    # Insert new news
    cursor.execute(add_news, data_news)

# Commit the transaction
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()
