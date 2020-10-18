# Introduction To Network Analysis
Istilah penting yang perlu dipahami adalah
1. nodes
nodes adalah objek/individu yang digambarkan dalam bentuk "titik".
2. edge
edge adalah garis yang menghubungkan satu objek ke objek lainnya sehingga digambarkan dalam bentuk "garis"
3. neighbors
neighbors adalah nodes-nodes yang terhubung dengan nodes tersebut.
4. degree (number of neighbors)
degree menunjukkan banyaknya tetangga dari nodes terkait.
5. degree_centrality 
merupakan perbandingan antara banyaknya tetangga yang dimiliki dan banyaknya tetangga yang mungkin dimiliki.
6. Betweenness_centrality
merupakan perbandingan antara banyaknya path terpendek dan banyaknya kemungkinan path terpendek
7. Cliques/Communalities
merupakan kumpulan dari nodes yang terhubung secara sempurna (Group of nodes that fully connected)
8. Maximum Cliques
merupakan clique yang jika ditambahkan suatu node, maka dia tidak lagi menjadi cliques.
9. Simplest cliques vs simplest complex cliques
the simplest cliques = edge, the simplest complex cliques = triangle
10. Open Triangle
Triangle yang masih belum terhubung secara penuh (sempurna). Open triangle ini bisa dilustrasikan kondisi "Jika A teman B, dan A teman C, maka kemungkinan B adalah teman C".

## Penggunaan Network Analysis
1. Shorthest Path
mencari path terpendek diantar dua nodes (bisa menggunakan Breadth-first Algorithm)
2. Find important users : nx.degree_centrality()
3. Find largest communities of collaborators : max_cliques()
4. recommmendation system : open triangle

