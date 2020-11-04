<template>
  <div class="container">
    <h1 class="text-center">Welcome to Chatire!</h1>
    <div class="row" id="auth-container">
      <div class="col-sm-4 offset-sm-4">
        <ul class="nav nav-tabs nav-justified" id="myTab" role="tablist">
          <li class="nav-item">
            <a aria-controls="signup" aria-selected="true" class="nav-link active" data-toggle="tab" href="#signup"
               id="signup-tab" role="tab">Sign Up</a>
          </li>
          <li class="nav-item">
            <a aria-controls="signin" aria-selected="false" class="nav-link" data-toggle="tab" href="#signin"
               id="signin-tab"
               role="tab">Sign In</a>
          </li>
        </ul>

        <div class="tab-content" id="myTabContent">

          <div aria-labelledby="signin-tab" class="tab-pane fade show active" id="signup" role="tabpanel">
            <form @submit.prevent="signUp">
              <div class="form-group">
                <input class="form-control" id="email" placeholder="Email Address" type="email"
                       v-model="email">
              </div>
              <div class="form-row">
                <div class="form-group col-md-6">
                  <input class="form-control" id="username" placeholder="Username" required type="text"
                         v-model="username">
                </div>
                <div class="form-group col-md-6">
                  <input class="form-control" id="password" placeholder="Password" required type="password"
                         v-model="password">
                </div>
              </div>
              <div class="form-group">
                <div class="form-check">
                  <input class="form-check-input" id="toc" required type="checkbox">
                  <label class="form-check-label" for="gridCheck">
                    Accept terms and Conditions
                  </label>
                </div>
              </div>
              <button class="btn btn-block btn-primary" type="submit">Sign up</button>
            </form>
          </div>

          <div aria-labelledby="signin-tab" class="tab-pane fade" id="signin" role="tabpanel">
            <form @submit.prevent="signIn">
              <div class="form-group">
                <input class="form-control" id="username" placeholder="Username" required type="text"
                       v-model="username">
              </div>
              <div class="form-group">
                <input class="form-control" id="password" placeholder="Password" required type="password"
                       v-model="password">
              </div>
              <button class="btn btn-block btn-primary" type="submit">Sign in</button>
            </form>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {getAuthURL} from "@/http-common";

export default {
  name: "UserAuth",
  data() {
    return {
      email: '', username: '', password: '',
    }
  },
  methods: {
    signUp() {
      // let url = "http://0.0.0.0:8000/dj-rest-auth/registration/"
      //  let body = {
      //    'email': this.email,
      //    'username': this.username,
      //    'password1': this.password,
      //    'password2': this.password
      //  }
      axios({
        method: 'post',
        baseURL: "http://0.0.0.0:8000/dj-rest-auth/registration/",
        headers: {
          common: {
            Accept: 'application/json',
          }
        },
        body: {
          'email': this.email,
          'username': this.username,
          'password1': this.password,
          'password2': this.password
        }
      }).then(response => {
        console.log(response)
      }).catch(error => {
        console.log(error)
      })
      // axios.post(url, body).then(() => {
      //   alert("Your account has been created. You will be signed in automatically")
      //   this.signIn()
      // })

    },
    signIn() {
      const credentials = {
        "username": this.username,
        "password": this.password
      }
      axios.post(getAuthURL("login"), credentials).then(response => {
        sessionStorage.setItem('authToken', response.data.key)
        sessionStorage.setItem('username', this.username)
        this.$router.push('/chats')
      })

    }
  }
}
</script>

<style scoped>
#auth-container {
  margin-top: 50px;
}

.tab-content {
  padding-top: 20px;
}
</style>
