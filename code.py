import os for dirname, _, filenames in os.walk('/kaggle/input'): for filename in filenames: print(os.path.join(dirname, filename))

import matplotlib.pyplot as plt import seaborn as sns

election_df = pd.read_csv('/kaggle/input/india-lok-sabha-election-results-2024/election_results_2024.csv') election_df.head() election_df.tail() election_df.shape election_df.describe() election_df.describe(include = 'object').transpose() election_df.info() election_df.isna().sum() election_df[election_df.isna().any(axis=1)] election_df['Margin'] = pd.to_numeric(election_df['Margin'], errors='coerce') election_df = election_df.fillna({'Trailing Candidate': 'N/A', 'Trailing Party': 'N/A', 'Margin': 0}) election_df[election_df['Constituency']=='Maharajganj'] election_df.loc[election_df['Constituency']=='Maharajganj', 'Constituency'] = ['Maharajganj(UP)', 'Maharajganj(Bihar)'] election_df.iloc[332:334] plt.figure(figsize = (10,6)) sns.countplot(data = election_df, x='Leading Party',order=election_df['Leading Party'].value_counts().index) plt.title('Number of Constituencies Each Leading Party Leads') plt.xticks(rotation = 90) plt.show() leading_party_counts = election_df['Leading Party'].value_counts() leading_party_counts others_counts = leading_party_counts[leading_party_counts<3].sum() others_counts leading_party_counts = leading_party_counts[leading_party_counts>=3] leading_party_counts['Others'] = others_counts

plt.figure(figsize=(10, 8)) wedges, _ = plt.pie(leading_party_counts, labels=None, startangle=140, textprops={'fontsize': 12}, wedgeprops=dict(width=0.7))

legend_labels = [f'{party} ({count} seats)' for party, count in zip(leading_party_counts.index, leading_party_counts)] plt.legend(wedges, legend_labels, title="Leading Party", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1)) plt.subplots_adjust(left=0.1, right=0.65)

plt.title('Share of Constituencies Each Leading Party Leads', fontsize=15) plt.show() plt.figure(figsize=(10, 6)) sns.histplot(data=election_df, x='Margin', bins=10, kde=True) plt.title('Distribution of Victory Margins') plt.show() top_20_winners = election_df.sort_values(by = 'Margin', ascending = False).head(20) from matplotlib.ticker import ScalarFormatter

plt.figure(figsize=(12, 8)) sns.barplot(x='Margin', y='Leading Candidate', data=top_20_winners, hue='Leading Party', dodge=False) plt.xlabel('Margin') plt.ylabel('Leading Candidate') plt.title('Top 20 Candidates with Highest Margin') plt.grid(axis='x', linestyle='--', alpha=0.7) plt.legend(title='Party', loc='lower right')

ax = plt.gca() ax.xaxis.set_major_formatter(ScalarFormatter())

ax.xaxis.get_major_formatter().set_scientific(False)

plt.tight_layout() plt.show() bottom_20_winners = election_df.sort_values(by = 'Margin', ascending = True).head(20) plt.figure(figsize=(12, 8)) sns.barplot(x='Margin', y='Leading Candidate', data=bottom_20_winners, hue='Leading Party', dodge=False) plt.xlabel('Margin') plt.ylabel('Leading Candidate') plt.title('Top 20 Candidates with Lowest Margin') plt.grid(axis='x', linestyle='--', alpha=0.7) plt.legend(title='Party', loc='lower right')

ax = plt.gca()

plt.gca().invert_yaxis()

ax.xaxis.set_major_formatter(ScalarFormatter()) ax.xaxis.get_major_formatter().set_scientific(False)

plt.tight_layout() plt.show()

ax.xaxis.get_major_formatter().set_scientific(False)

plt.show()
