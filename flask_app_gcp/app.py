from flask import Flask, render_template
from google.cloud import storage

app = Flask(__name__)

# Replace 'your-bucket-name' with your actual GCP Storage bucket name
bucket_name = 'axona-hs1'
from openai import OpenAI

client = OpenAI(api_key='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')
def download_blob(blob_name):
    """Downloads a blob from the GCP Storage bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Download the blob's content as a string
    content = blob.download_as_text()

    return content

final_score = []
names = []
def election(content):
    for i in content.split("||||"):
        # print(i)
        res_scr = eval(i.split("<<<")[0])[0]
        test_scr = eval(i.split("<<<")[1].split("&&")[0])[0]
        name =  i.split("<<<")[1].split("&&")[1]
        # print(name)
        names.append(name)
        s_max = res_scr + test_scr
        final_score.append(s_max)
        # print(res_scr)
        # print(test_scr)
        # print(names)
        elected = final_score.index(max(final_score))
        return str(names[elected])

def HTML_formatter(text):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
         
{"role": "system", "content": "You excel as an HTML coder and text formatter, ensuring precision and creativity in your work."},
{"role": "user", "content": "Your task is to meticulously format the given text for seamless integration into an HTML page, focusing solely on the body part. The provided data is: " + str(text) },
{"role": "user", "content": "Emphasize a contemporary, elegant, and visually appealing design to enhance the overall aesthetic."},
{"role": "user", "content": "I emphasize the importance of avoiding any unnecessary descriptions or extraneous text that may detract from the sleek and modern presentation."},

{"role": "user", "content": "For the text formatting:"},
{"role": "user", "content": "- Utilize <strong> tags for bold text, enhancing key points."},
{"role": "user", "content": "- Employ appropriate <h1>, <h2>, and <p> tags for headlines, titles, subtitles, and normal text respectively."},
{"role": "user", "content": "- Consider using color attributes to highlight specific sections, ensuring a tasteful and cohesive color scheme."},
{"role": "user", "content": "- Pay careful attention to alignment, maintaining a sense of balance and readability throughout the content."},
{"role": "user", "content": "- Strive for a harmonious blend of these elements to achieve a polished and professional appearance."}





        ]
    )
    return completion.choices[0].message.content

@app.route('/')
def index():
    out = []
    # Replace 'your-file-name.txt' with the actual file name you want to fetch
    file_names = ['filtered_dir/numbers.txt', 'filtered_dir/text.txt']
    try:
        for n, i in enumerate(file_names):
            try:
                content = download_blob(i)
                print(n)
                if n==0:
                    content = election(content)
                    out.append(content)
                else:
                    out.append(content)
                    
                    # print(content)
                # election(content)
            except:
                pass

            # try:
            #     content = download_blob(file_name)
                #    print("resume_score:",eval(i.split("<<<")[0])[0])
        # print(out)
        # print(out[1].split("other analysis"))
        out = HTML_formatter(out)
        print(out)
        return render_template('index.html', content=str(out))
    except Exception as e:
        return f"Error fetching data: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=3000)
