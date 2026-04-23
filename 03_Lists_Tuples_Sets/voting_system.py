# task 11 voting system mini project

vote_list = [
"Mohsin Rizvi","Mohsin Rizvi","Mohsin Rizvi","Mohsin Rizvi","Mohsin Rizvi",
"Mohsin Rizvi","Mohsin Rizvi","Mohsin Rizvi","Mohsin Rizvi","Mohsin Rizvi",
"Mohsin Rizvi","Mohsin Rizvi","Mohsin Rizvi","Mohsin Rizvi","Mohsin Rizvi",
"Mohsin Rizvi","Mohsin Rizvi","Mohsin Rizvi",

"Amjad Zaidi","Amjad Zaidi","Amjad Zaidi","Amjad Zaidi","Amjad Zaidi",
"Amjad Zaidi","Amjad Zaidi","Amjad Zaidi","Amjad Zaidi","Amjad Zaidi",
"Amjad Zaidi","Amjad Zaidi",

"Iqbal Hassan","Iqbal Hassan","Iqbal Hassan","Iqbal Hassan","Iqbal Hassan",
"Iqbal Hassan","Iqbal Hassan","Iqbal Hassan","Iqbal Hassan","Iqbal Hassan",

"Dr Maisum","Dr Maisum","Dr Maisum","Dr Maisum","Dr Maisum",
"Dr Maisum","Dr Maisum","Dr Maisum",

"GM Parvi","GM Parvi","GM Parvi","GM Parvi","GM Parvi",
"GM Parvi","GM Parvi","GM Parvi","GM Parvi","GM Parvi","GM Parvi","GM Parvi"
]

# Step 1: Get unique candidates
candidates = list(set(vote_list))

# Step 2: Count votes
vote_count = {}

for candidate in candidates:
    vote_count[candidate] = vote_list.count(candidate)

# Step 3: Display results
for candidate in vote_count:
    print(candidate, "got", vote_count[candidate], "votes.")

# Step 4: Find winner
winner = max(vote_count, key=vote_count.get)

print("Winner is:", winner, "with", vote_count[winner], "votes!!")