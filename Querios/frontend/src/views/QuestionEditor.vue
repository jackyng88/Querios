<template>
  <div class="container mt-2">
    <h1 class="mb-3">Ask a Question</h1>
    <form @submit.prevent="onSubmit">
      <textarea 
        v-model="question_body"
        class="form-control"
        placeholder="Have a question to ask?"
        rows="3">
      </textarea>
      <br>
      <button 
        type="submit"
        class="btn btn-success">
        Publish
      </button>
    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
</template>



<script>
import { apiService } from "@/common/api.service.js"
export default {
  name: "QuestionEditor",
  props: {
    slug: {
      type: String,
      required: false
    }
  },
  data () {
    return {
      question_body: null,
      error: null
    }
  },
  methods: {
    onSubmit() {
      if (!this.question_body) {
        this.error = "Question can't be empty!";
      }
      else if (this.question_body.length > 512) {
        this.error = "Question length can not exceed 512 characters!";
      }
      else {
        let endpoint = "/api/questions/";
        let method = "POST";
        if (this.slug !== undefined) {
          endpoint += `${this.slug}/`;
          method = "PUT"
        }
        // apiService function calls the endpoint, method, and the question then uses Vue router
        // to redirect back to the question with a slug that we just created.
        apiService(endpoint, method, { content: this.question_body })
          .then(question_data => { 
            this.$router.push({ 
              name: 'question', 
              params: { slug: question_data.slug }})
          })
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    if (to.params.slug !== undefined) {
      let endpoint = `/api/questions/${ to.params.slug }/`;
      let data = await apiService(endpoint);
      return next(vm => (vm.question_body = data.content))
    } 
    else {
      return next();
    }   
  },
  created() {
    document.title = "Querios - Editor";
  }
}
</script>