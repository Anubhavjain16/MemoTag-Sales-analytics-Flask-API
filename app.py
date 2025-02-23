from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging
import pandas as pd
import io

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024  # 16MB max file size

# Configure Gemini
try:
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    logger.error(f"Error configuring Gemini: {str(e)}")

def analyze_csv_data(df):
    """Analyze the CSV data and return key insights"""
    try:
        analysis = {
            'total_rows': len(df),
            'columns': list(df.columns),
            'summary': df.describe().to_dict(),
            'sample_data': df.head().to_dict()
        }
        return analysis
    except Exception as e:
        logger.error(f"Error analyzing CSV data: {str(e)}")
        return None

def generate_response(prompt, data_context=None):
    try:
        if data_context:
            prompt = f"""Based on the following data analysis:
            {data_context}
            
            {prompt}"""
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        raise

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/upload-csv', methods=['POST'])
def upload_csv():
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'}), 400
        
        if not file.filename.endswith('.csv'):
            return jsonify({'success': False, 'error': 'Please upload a CSV file'}), 400
        
        # Read CSV file
        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        df = pd.read_csv(stream)
        
        # Analyze the data
        analysis = analyze_csv_data(df)
        if analysis:
            return jsonify({'success': True, 'analysis': analysis})
        else:
            return jsonify({'success': False, 'error': 'Failed to analyze CSV data'}), 500
            
    except Exception as e:
        logger.error(f"Error processing CSV upload: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/sales-recommendations', methods=['POST'])
def get_sales_recommendations():
    data_context = request.json.get('analysis', None)
    
    prompt = """Based on the provided sales data analysis, provide 10 specific, data-driven recommendations 
    to increase sales. Focus on actionable insights that directly relate to the patterns and trends shown 
    in the data. Format the response as a numbered list."""
    
    try:
        recommendations = generate_response(prompt, data_context)
        logger.info("Successfully generated sales recommendations")
        return jsonify({
            'success': True,
            'data': recommendations
        })
    except Exception as e:
        logger.error(f"Error generating sales recommendations: {str(e)}")
        return jsonify({
            'success': False,
            'error': "Failed to generate recommendations. Please try again."
        }), 500

@app.route('/api/sales-strategies', methods=['POST'])
def get_sales_strategies():
    data_context = request.json.get('analysis', None)
    
    prompt = """Based on the provided sales data analysis, provide 3 detailed, data-driven sales strategies. 
    Each strategy should include specific steps for implementation and expected outcomes based on the 
    patterns and trends in the data. Format the response as a numbered list."""
    
    try:
        strategies = generate_response(prompt, data_context)
        logger.info("Successfully generated sales strategies")
        return jsonify({
            'success': True,
            'data': strategies
        })
    except Exception as e:
        logger.error(f"Error generating sales strategies: {str(e)}")
        return jsonify({
            'success': False,
            'error': "Failed to generate strategies. Please try again."
        }), 500

@app.route('/api/marketing-funnels', methods=['POST'])
def get_marketing_funnels():
    data_context = request.json.get('analysis', None)
    
    prompt = """Based on the provided sales data analysis, create 5 targeted marketing funnels/strategies. 
    Include specific channels, targeting approaches, and conversion optimization techniques that align with 
    the patterns and customer behaviors shown in the data. Format the response as a numbered list."""
    
    try:
        funnels = generate_response(prompt, data_context)
        logger.info("Successfully generated marketing funnels")
        return jsonify({
            'success': True,
            'data': funnels
        })
    except Exception as e:
        logger.error(f"Error generating marketing funnels: {str(e)}")
        return jsonify({
            'success': False,
            'error': "Failed to generate marketing funnels. Please try again."
        }), 500

if __name__ == '__main__':
    app.run(debug=True)