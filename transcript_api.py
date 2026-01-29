from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/get_transcript")
def get_transcript():
    video_id = request.args.get("videoId")
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(videoId=
Agvu-AiQLm0)
        transcript_text = " ".join([t['text'] for t in transcript_list])
        return jsonify({"transcriptText": transcript_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
