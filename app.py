# import awsgi
# import os
# import json
import logging
import flask
from flask import Blueprint, render_template
from dotenv import load_dotenv, find_dotenv

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)
log.info(f'load env: {load_dotenv(find_dotenv())}')

app = flask.Flask(__name__, static_url_path='/assets', static_folder='templates/assets')


# @app.route("/")
# def index():
#     query_responses_json = database_helpers.get_qnr()
#     return flask.render_template('index.html', queryResponses=query_responses_json)


@app.route("/")
def index():
    context = {
		# "page_title" : page_title,
		# "student_name": enrollment.user.name,
		# "course_name": enrollment.subscription.course.title,
		# "course_fee": float(enrollment.fee),
		# "discount_fee": float(enrollment.discount),
		# "total_fee": float(enrollment.total_fee),
		# "is_initial_payment": not enrollment.due_amount,
		# "pending_amount": pending_amount,
		# "enrollment_id" : enrollment_id,
		# "paid_amount" : paid_amount,
		# 'payments': payments,
	}
    return render_template('index.html', context=context)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/single-blog')
def single_blog():
    return render_template('single-blog.html')

@app.route('/single-product')
def single_product():
    return render_template('single-product.html')

# @app.route("/get_hash_query_map")
# def get_hash_query_map():
#     print('start get_hash_query_map')
#     hash_map = database_helpers.get_qnr(hash_map=True)
#     print(hash_map)
#     return flask.jsonify(hash_map)


# @app.route("/view_grievances")
# async def view_grievances():
#     grievance_records = database_helpers.get_grievance_records()
#     return flask.render_template('table_view.html', queryResponses=grievance_records)


# @app.route("/export_records", methods=['POST'])
# def export_grievance_records():
#     data = flask.request.get_json()
#     selected_ids = data.get('ids', [])
#     print(f'selected_ids to export: {selected_ids}')
#     grievance_records = database_helpers.get_grievance_records()
#     selected_responses = [record for record in grievance_records if record['id'] in selected_ids]
#     print(f'{len(selected_responses)} selected_responses: {selected_responses}')
#     output = rule_helpers.download_csv(selected_responses)
#     filename = 'grievances.csv'
#     response = flask.Response(output.getvalue(), mimetype='text/csv')
#     response.headers['Content-Disposition'] = f'attachment; filename={filename}'
#     return response


# @app.route("/delete_records", methods=['POST'])
# def delete_grievance_records():
#     data = flask.request.get_json()
#     selected_ids = data.get('ids', [])
#     print(f'selected_ids to delete: {selected_ids}')
#     database_helpers.remove_records_batch_boto(selected_ids)
#     return flask.redirect('/view_grievances')


# @app.route("/add_query")
# async def add_query():
#     print("called /add_query")
#     return flask.render_template('add_query.html')


# @app.route("/submit_response", methods=['POST'])
# async def submit_response():
#     record = dict(flask.request.form)
#     print(f"new record: {record}")
#     database_helpers.merge_insert_record_boto(record)
#     return flask.redirect(BASE_PATH)


# @app.route("/get_edit_response", methods=['POST'])
# async def get_edit_response():
#     record = dict(flask.request.form)
#     print(f"edit record: {record}")
#     return flask.render_template('edit_query.html', query_response=record)


# @app.route("/edit_query_response", methods=['POST'])
# async def edit_query_response():
#     record = dict(flask.request.form)
#     print(f"edited record: {record}")
#     database_helpers.merge_insert_record_boto(record)
#     return flask.redirect(BASE_PATH)


# @app.route("/remove_query", methods=['POST'])
# async def remove_query():
#     data = flask.request.get_json()
#     print(f'data to delete: {data}')
#     selected_hashes = data.get('hashes', [])
#     print(f'selected_hashes to delete: {selected_hashes}')
#     database_helpers.remove_record_boto(selected_hashes)
#     return flask.redirect(BASE_PATH)
#     # record = flask.request.json
#     # print(f"remove record: {record}")
#     # database_helpers.remove_record_boto(record)
#     # return flask.jsonify(record)


if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True, port=8080)
