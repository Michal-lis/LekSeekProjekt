Vue.config.delimiters = ["[[", "]]"]

var demo = new Vue({
    el: "#app",
    data: {
        'apptitle': ' Leaving feedback',
        'comments': []//pusty array na commenty
    },
    methods: {
        addComment: function () {
            var newComment = {
                commentseans: this.commentseans.trim(),
                commentauthor: this.commentauthor.trim(),
                commentopinion: this.commentopinion.trim(),
                commentmark: this.commentmark.trim()
            };

            this.$http.post('http://127.0.0.1:8000/api/comments/', newComment);
        },
        removeComment: function (index) {
            this.$http.delete('http://127.0.0.1:8000/api/comments/'.concat(this.jobs[index].id));
            this.comments.splice(index, 1);
        }
    },
    ready: function () {
        this.$http.get('http://127.0.0.1:8000/api/jobs/').then(function (response) {
                this.jobs = response.data;
            },
            function (response) {
                console.log(response);
            });
    }
});
}
})
