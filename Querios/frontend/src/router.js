import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Question from "./views/Question.vue";
import QuestionEditor from "./views/QuestionEditor.vue";
import AnswerEditor from "./views/AnswerEditor.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  // base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      // :slug is an example of how you define parameters in paths.
      path: "/question/:slug",
      name: "question",
      component: Question,
      props: true
    },
    {
      path: "/ask",
      name: "question-editor",
      component: QuestionEditor
    },
    {
      path: "/answer/:id",
      name: "answer-editor",
      component: AnswerEditor,
      props: true
    },
  ]
});


