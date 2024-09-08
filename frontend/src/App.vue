<template>
  <div id="app">
    <h1>Discord Messages</h1>
    <button @click="fetchMessages">Fetch Messages</button>
    <ul>
      <li v-for="message in messages" :key="message.id">
        {{ message.author }}: {{ message.content }} ({{ message.timestamp }})
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: []
    };
  },
  methods: {
    async fetchMessages() {
      try {
        const response = await this.$http.get('http://localhost:5000/messages')  // Flask API URL
        this.messages = response.data
      } catch (error) {
        console.error('Error fetching messages:', error)
      }
    }
  }
};
</script>
