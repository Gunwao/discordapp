# Use the official Node.js image as the base image
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the frontend source code
COPY . .

# Expose port 8080 for Vue.js development server
EXPOSE 8080

# Start the Vue.js app in development mode with hot-reloading
CMD ["npm", "run", "serve"]
