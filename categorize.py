import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def calculate_thresholds(data, m1, m2):
    best_accuracy = 0
    best_t1 = 0
    best_t2 = 0
    counts = data[m1 + ' category'].value_counts()
    c1 = counts[1]
    c2 = counts[2]
    c3 = counts[3]
    # print(counts)
    # print(c1, c2, c3)

    d = data.sort_values(by=[m2], inplace=False, ascending=True)
    d = d.reset_index(drop=True)
    # print(d.head(30))

    categories = [0, 0, 0, 0, 0, 0, c1, c2, c3]

    for t2, row2 in d.iterrows():
        categories[2 + row2[m1 + ' category']] += 1
        categories[5 + row2[m1 + ' category']] -= 1
        for t1, row1 in d.iterrows():
            if t1 >= t2:
                break
            categories[2 + row1[m1 + ' category']] -= 1
            categories[row1[m1 + ' category'] - 1] += 1
            categories[8] = c3 - categories[2] - categories[5]
            acc = (categories[0] + categories[4] + categories[8]) / (c1 + c2 + c3)
            if acc > best_accuracy:
                best_accuracy = acc
                best_t1 = row1[m2]
                best_t2 = row2[m2]
        categories[3] += categories[0]
        categories[4] += categories[1]
        categories[5] += categories[2]
        categories[0] = 0
        categories[1] = 0
        categories[2] = 0

    return best_t1, best_t2, best_accuracy


def graph_category_comparison(data, m1, m2, data_name):
    df = data.groupby([m1 + ' category', m2 + ' category']).size().reset_index(name='count')

    fig = px.bar(df, x=m1 + " category", y="count", color=m2 + " category",
                 title=m1 + " " + m2 + " category comparison " + data_name)
    fig.show()


def graph_score_comparison(data, m1, m2, data_name):
    fig = go.Figure(
        data=go.Scatter(x=data[m2], y=data[m1], mode='markers', text=data['password']))
    fig.update_layout(
        title={
            'text': m1 + ' - ' + m2 + ' comparison' + data_name,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.update_yaxes(type="log")
    fig.update_layout(xaxis_title=m2, yaxis_title=m1, )
    fig.show()


def graph_category_score_comparison(data, m1, m2, data_name):
    data['graphtext'] = data['password'] + '|' + data[m1].astype(str)
    fig = go.Figure(
        data=go.Scatter(x=data[m2], y=data[m1 + ' category'], mode='markers', text=data['graphtext']))
    fig.update_layout(
        title={
            'text': m1 + ' group - ' + m2 + ' score comparison, ' + data_name,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.update_layout(xaxis_title=m2, yaxis_title=m1 + " group", )
    fig.show()


def category_statistics(data, m1, m2):
    data1 = data[m2].loc[data[m1 + ' category'] == 1]
    data2 = data[m2].loc[data[m1 + ' category'] == 2]
    data3 = data[m2].loc[data[m1 + ' category'] == 3]

    print('Category 1:')
    print(data1.describe())
    print('Category 2:')
    print(data2.describe())
    print('Category 3:')
    print(data3.describe())


def calculate_accuracy(data, m1, m2):
    cat1 = m1 + ' category'
    cat2 = m2 + ' category'
    n = len(data)

    n1 = data[(data[cat1] == 1) & (data[cat2] == 1)].count()[1]
    n2 = data[(data[cat1] == 2) & (data[cat2] == 2)].count()[1]
    n3 = data[(data[cat1] == 3) & (data[cat2] == 3)].count()[1]

    n5 = data[(data[cat1] == 1) & (data[cat2] == 2)].count()[1] + \
         data[(data[cat1] == 1) & (data[cat2] == 3)].count()[1] + \
         data[(data[cat1] == 2) & (data[cat2] == 3)].count()[1]

    n6 = data[(data[cat1] == 3) & (data[cat2] == 2)].count()[1] + \
         data[(data[cat1] == 3) & (data[cat2] == 1)].count()[1] + \
         data[(data[cat1] == 2) & (data[cat2] == 1)].count()[1]

    return (n1 + n2 + n3) / n, n5 / n, n6 / n


def save_misclassifications(data):
    pass


def calculate_category(score, t1, t2):
    if score == -5:
        return 3
    elif score <= t1:
        return 1
    elif score <= t2:
        return 2
    else:
        return 3


def categorize(method, data, t1, t2):
    data[method + ' category'] = data.apply(lambda row: calculate_category(row[method], t1, t2), axis=1)
    return data


def run():
    # testovacia sada 1
    test1_data = pd.read_excel(testDS1X)
    test1_data = categorize(method1, test1_data, threshold1, threshold2)
    if_thresholds = calculate_thresholds(test1_data, method1, method2)
    # if_thresholds = [43312, 52279, 58]
    test1_data = categorize(method2, test1_data, if_thresholds[0], if_thresholds[1])
    print(if_thresholds)

    # testovacia sada 2
    test2_data = pd.read_excel(testDS2X)
    test2_data = categorize(method1, test2_data, threshold1, threshold2)
    test2_data = categorize(method2, test2_data, if_thresholds[0], if_thresholds[1])

    # statistiky
    category_statistics(test1_data, method1, method2)
    stat1 = calculate_accuracy(test1_data, method1, method2)
    stat2 = calculate_accuracy(test2_data, method1, method2)
    print('TEST DATASET1 \nAccuracy:', stat1[0], '\nOverrated:', stat1[1], '\nUnderrated:', stat1[2])
    print('TEST DATASET2 \nAccuracy:', stat2[0], '\nOverrated:', stat2[1], '\nUnderrated:', stat2[2])
    save_misclassifications(test2_data)

    # grafy
    graph_score_comparison(test1_data, method1, method2, 'Test data 1')
    graph_score_comparison(test2_data, method1, method2, 'Test data 2')
    graph_category_score_comparison(test1_data, method1, method2, 'Test data 1')
    graph_category_score_comparison(test2_data, method1, method2, 'Test data 2')
    graph_category_comparison(test1_data, method1, method2, 'Test data 1')
    graph_category_comparison(test2_data, method1, method2, 'Test data 2')


########
dataset_path = 'datasets/clean/'
testDS1X = dataset_path + 'test/test_set12.xlsx'
testDS2X = dataset_path + 'test/test_set2.xlsx'
threshold1 = 10 ** 6
threshold2 = 10 ** 12

method1 = 'pcfg'
method2 = 'if'

run()
