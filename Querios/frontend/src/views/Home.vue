<template>
  <div class="home">
    <div class="container mt-2">
      <div v-for="question in questions"
           :key="question.pk">
        <p class="mb-0">Posted by:
          <span class="question-author">{{ question.author }}</span>
        </p>
        <h2>
          <!-- Vue router-link to the question component to allow viewing of single question instances. -->
          <router-link 
            :to="{ name: 'question', params: { slug: question.slug }}"
            class="question-link">
            {{ question.content }}
          </router-link>
        </h2>
        <p>Answers: {{ question.answers_count }}</p>
        <hr>
      </div>
      <div class="my-4">
        <p v-show="loadingQuestions">...loading...</p>
        <button v-show="next"
                @click="getQuestions"
                class="btn btn-sm btn-outline-success">
                Load More
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js"

export default {
  name: "home",
  data : function () {
    return {
      questions: [],
      next: null,
      loadingQuestions: false
    }
  },
  methods: {
    getQuestions() {
      /* 
      makes a GET request to the questions list API endpoint. 
      When this getQuestions methos is called for the first time by the Vue created()
      lifecycle hook, we check if there's another page with the if (data.next) block.
      If it exists, it says this.next to that endpoint's next. We can then call a 
      loadMore button to load more questions which calls if (this.next){ endpoint = this.next;}
      */
      let endpoint = "api/questions/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      apiService(endpoint)
        .then(data => {
          this.questions.push(...data.results)
          // Our REST API response from Django has a next field that we can use to assign
          // to the next field. We also need to set loadingQuestion back to false after the push.
          this.loadingQuestions = false;
          if (data.next) {
            this.next = data.next;
          }
          else {
            this.next = null;
          }
        })
    }
  },
  // Vue created lifecycle hook
  created() {
    this.getQuestions()
    document.title = "Querios";
  }
};
</script>


<style scoped>
  .question-author {
    font-weight: bold;
    color: #DC3545;
  }

  .question-link {
    font-weight: bold;
    color: black;
  }

  .question-link:hover {
    color: #343A40;
    text-decoration: none;
  }
</style>

