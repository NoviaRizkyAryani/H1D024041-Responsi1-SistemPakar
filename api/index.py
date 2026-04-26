from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/pakar', methods=['POST'])
def pakar():
    try:
        data = request.get_json()
        
        skor = {
            "Kos Sultan": 0,
            "Kos Hemat": 0,
            "Kos Nongkrong": 0,
            "Kos Privat": 0,
            "Kos Tertib": 0
        }

        mapping = {
            'q1': {'A': 'Kos Hemat', 'B': 'Kos Nongkrong', 'C': 'Kos Sultan'},
            'q2': {'A': 'Kos Hemat', 'B': 'Kos Privat'},
            'q3': {'A': 'Kos Privat', 'B': 'Kos Nongkrong'},
            'q4': {'A': 'Kos Hemat', 'B': 'Kos Sultan'},
            'q5': {'A': 'Kos Hemat', 'B': 'Kos Sultan'}, 
            'q6': {'A': 'Kos Privat', 'B': 'Kos Hemat'},
            'q7': {'A': 'Kos Sultan', 'B': 'Kos Tertib'},
            'q8': {'A': 'Kos Hemat', 'B': 'Kos Tertib'},
            'q9': {'A': 'Kos Nongkrong', 'B': 'Kos Tertib'},
            'q10': {'A': 'Kos Tertib', 'B': 'Kos Nongkrong'},
            'q11': {'A': 'Kos Hemat', 'B': 'Kos Privat'},
            'q12': {'A': 'Kos Hemat', 'B': 'Kos Sultan'},
            'q13': {'A': 'Kos Hemat', 'B': 'Kos Sultan'},
            'q14': {'A': 'Kos Hemat', 'B': 'Kos Privat'},
            'q15': {'A': 'Kos Hemat', 'B': 'Kos Sultan'},
            'q16': {'A': 'Kos Privat', 'B': 'Kos Hemat'}
        }
    
        for q_key, choice in data.items():
            if q_key in mapping and choice in mapping[q_key]:
                target = mapping[q_key][choice]
                skor[target] += 10 

        total_possible = 160
        match_percentages = {k: round((v / total_possible) * 100, 1) for k, v in skor.items()}
        
        hasil_utama = max(skor, key=skor.get)
        
        descriptions = {
            "Kos Sultan": "Fasilitas nomor satu! Cocok buat kamu yang pengen fokus nugas dengan AC dingin dan privasi penuh tanpa mikirin budget.",
            "Kos Hemat": "Dompet aman, kuliah lancar! Cocok buat yang pengen deket kampus dan cuma butuh kamar buat istirahat.",
            "Kos Nongkrong": "Banyak temen, banyak cerita! Cocok buat kamu yang ekstrovert dan seneng punya lingkungan kos yang solid dan seru.",
            "Kos Privat": "Bebas berekspresi! Cocok buat kamu yang butuh kamar luas buat naruh PC/peralatan kuliah dan pengen ketenangan total.",
            "Kos Tertib": "Belajar jadi tenang! Cocok buat kamu yang mengutamakan keamanan dan lingkungan yang tertib biar kuliah makin fokus."
        }

        return jsonify({
            'success': True,
            'hasil': hasil_utama,
            'deskripsi': descriptions[hasil_utama],
            'stats': match_percentages
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)