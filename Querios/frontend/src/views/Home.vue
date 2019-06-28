<template>
  <div class="home">
    <div class="container">
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
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js"

export default {
  name: "home",
  data : function () {
    return {
      questions: []
    }
  },
  methods: {
    getQuestions() {
      let endpoint = "api/questions/";
      apiService(endpoint)
        .then(data => {
          this.questions.push(...data.results)
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

