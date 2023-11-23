<template>
    <div class="home-image">
      <img src="src/assets/images/home.jpg" alt="">
    </div>
      <body>
        <div class="login-wrapper login_form form-container" style="width: 400px; height: 400px; background-color: #f4f4f4; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); padding: 20px;">
    <h2 style="margin-bottom: 20px; text-align: center; color: #333;">로그인</h2>
    <form style="height: 100%; display: flex; flex-direction: column; justify-content: center;">
      <input type="text" v-model.trim="username" placeholder="아이디" class="login-input">
      <input type="password" v-model.trim="password" placeholder="비밀번호" class="login-input">
      <button @click="logIn" type="submit" class="login-button">로그인</button>
    </form>
  </div>
  
    </body>
    </template>
    
    <script setup>
      import { useCounterStore } from '@/stores/counter';
      const store = useCounterStore()
    </script>
    
    <style scoped>
    .container {
      position: relative;
    }
    
    .form-container {
      position: absolute;
      top: 50%; /* Adjust as needed */
      left: 50%; /* Adjust as needed */
      transform: translate(-50%, -50%);
      z-index: 2;
      border: 1px solid black;
      border-radius: 15px;
      background-color: rgb(238, 235, 235);
    }
    .home-image{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      z-index: -1;
      opacity: 0.8;
    }
    
    
    /* 로그인  css */
    *{
        padding: 0;
        margin: 0;
        border: none;
    }
    body{
        font-size: 14px;
        font-family: 'Roboto', sans-serif;
    }
    .login-wrapper{
        width: 400px;
        height: 350px;
        padding: 40px;
        box-sizing: border-box;
    }
    
    .login-wrapper > h2{
        font-size: 24px;
        color: #a3b3f7;
        margin-bottom: 20px;
    }
    #login-form > input{
        width: 100%;
        height: 48px;
        padding: 0 10px;
        box-sizing: border-box;
        margin-bottom: 16px;
        border-radius: 6px;
        background-color: #F8F8F8;
    }
    #login-form > input::placeholder{
        color: #D2D2D2;
    }
    #login-form > input[type="submit"]{
        color: #fff;
        font-size: 16px;
        background-color: #aae8f8;
        margin-top: 20px;
    }
    
    #login-form > input[type="checkbox"]{
        display: none;
    }
    #login-form > label{
        color: #999999;
    }
    #login-form input[type="checkbox"] + label{
        cursor: pointer;
        padding-left: 26px;
        background-image: url("checkbox.png");
        background-repeat: no-repeat;
        background-size: contain;
    }
    #login-form input[type="checkbox"]:checked + label{
        background-image: url("checkbox-active.png");
        background-repeat: no-repeat;
        background-size: contain;
    }
  
  
    /* Add these styles to your existing styles or in a separate style block */
  
    .login-input {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 5px;
      box-sizing: border-box;
    }
  
    .login-button {
      background-color: #4caf50;
      color: #fff;
      border: none;
      padding: 10px;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s;
    }
  
    .login-button:hover {
      background-color: #45a049;
    }
    </style>