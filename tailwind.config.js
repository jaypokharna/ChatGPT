/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      colors:{
        chatbg : {50 : '#343541'},
        leftwin : '#202123',
        midbtncolor : '#3E3F4B',
        belchatbtn : '#202123',
        msgbox : '#40404E',
        sendmsg : '#8F8FA0',
        newchat : {10:'#3E3F4B'},
        chats : '#40404E',
        answer : '#444654'
      }
    },
  },
  plugins: [],
}

