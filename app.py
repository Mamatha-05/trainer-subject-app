from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

trainers = []
subjects = []
next_trainer_id = 1
next_subject_id = 1

@app.route('/add_trainer', methods=['GET', 'POST'])
def add_trainer():
    global next_trainer_id
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = request.get_json()
            name = data.get('name')
            expertise = data.get('expertise', '').split(',')
            if name:
                trainer = {'id': next_trainer_id, 'name': name, 'expertise': [e.strip() for e in expertise]}
                trainers.append(trainer)
                next_trainer_id += 1
                return jsonify({'message': f'Trainer "{name}" added successfully', 'trainer': trainer})
            else:
                return jsonify({'error': 'Name is required'}), 400
        else:
            name = request.form['name']
            expertise = request.form['expertise'].split(',')
            trainer = {'id': next_trainer_id, 'name': name, 'expertise': [e.strip() for e in expertise]}
            trainers.append(trainer)
            next_trainer_id += 1
            return jsonify({'message': f'Trainer "{name}" added successfully', 'trainer': trainer})
    return render_template('add_trainer.html')

@app.route('/trainer')
def get_trainers():
    return jsonify({'trainers': trainers})

@app.route('/trainer/<int:trainer_id>', methods=['GET', 'DELETE'])
def get_trainer(trainer_id):
    trainer = next((t for t in trainers if t['id'] == trainer_id), None)
    if trainer:
        if request.method == 'DELETE':
            trainers.remove(trainer)
            return jsonify({'message': f'Trainer "{trainer["name"]}" with ID {trainer_id} deleted successfully'})
        return jsonify({'trainer': trainer})
    return jsonify({'error': 'Trainer not found'}), 404

@app.route('/trainer/subject')
def get_trainers_by_subject():
    subject_name = request.args.get('name')
    if subject_name:
        relevant_trainers = [t for t in trainers if subject_name.lower() in [e.lower() for e in t['expertise']]]
        return jsonify({'trainers': relevant_trainers, 'subject': subject_name})
    return jsonify({'error': 'Subject name parameter is missing'}), 400

@app.route('/add_subject', methods=['GET', 'POST'])
def add_subject():
    global next_subject_id
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = request.get_json()
            name = data.get('name')
            if name:
                subject = {'id': next_subject_id, 'name': name}
                subjects.append(subject)
                next_subject_id += 1
                return jsonify({'message': f'Subject "{name}" added successfully', 'subject': subject})
            else:
                return jsonify({'error': 'Subject name is required'}), 400
        else:
            name = request.form['name']
            subject = {'id': next_subject_id, 'name': name}
            subjects.append(subject)
            next_subject_id += 1
            return jsonify({'message': f'Subject "{name}" added successfully', 'subject': subject})
    return render_template('add_subject.html')

@app.route('/subject')
def get_subjects():
    return jsonify({'subjects': subjects})

@app.route('/subject/<int:subject_id>')
def get_subject(subject_id):
    subject = next((s for s in subjects if s['id'] == subject_id), None)
    if subject:
        teaching_trainers = [t for t in trainers if subject['name'].lower() in [e.lower() for e in t['expertise']]]
        return jsonify({'subject': subject, 'taught_by_trainers': teaching_trainers})
    return jsonify({'error': 'Subject not found'}), 404

@app.route('/list_trainers')
def show_trainers_list():
    return render_template('list_trainers.html')

@app.route('/list_subjects')
def show_subjects_list():
    return render_template('list_subjects.html')

@app.route('/get_trainer_form')
def show_get_trainer_form():
    return render_template('get_trainer.html')

@app.route('/delete_trainer_form')
def show_delete_trainer_form():
    return render_template('delete_trainer.html')

@app.route('/find_trainers_by_subject_form')
def show_find_trainers_by_subject_form():
    return render_template('find_trainers_by_subject.html')

@app.route('/get_subject_form')
def show_get_subject_form():
    return render_template('get_subject.html')

@app.route('/')
def index():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)