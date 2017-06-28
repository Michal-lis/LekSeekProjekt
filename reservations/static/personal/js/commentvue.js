Vue.config.delimiters = ["[[", "]]"]


var demo = new Vue({
        el: "#app",
        data: {
            'comments': []//pusty array na commenty
        },
        methods: {
            addComment: function () {
                var newComment = {
                    commentseans: this.seans.trim(),
                    commentauthor: this.author.trim(),
                    commentopinion: this.opinion.trim(),
                    commentmark: this.mark.trim()
                };
                window.alert("dodajesz komentarz");
                this.$http.post('http://127.0.0.1:8000/api/comments/', newComment);
            },
            clearContents: function (element) {
                element.value = '';
            },
            removeComment: function (index) {
                this.$http.delete('http://127.0.0.1:8000/api/comments/'.concat(this.comments[index].id));
                this.comments.splice(index, 1);
            }
        },
        ready: function () {
            this.$http.get('http://127.0.0.1:8000/api/comments/').then(function (response) {
                    this.comments = response.data;
                },
                function (response) {
                    console.log(response);
                });
        }
    })
;
