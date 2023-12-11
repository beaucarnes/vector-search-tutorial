<template>
  <div>
  <div class="search-area">
      <div class="search-text">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search for accommodations..."
        class="search-input"
      />
      
      <button @click="fetchListings" class="search-button">Search</button>
      </div>
      <div class="filters">
  <!-- Show the free text input field only when the toggle is ON -->
  <div v-if="useFreeTextFilter" class="free-text-filter">
    <label for="freeTextFilter">Free Text Filter:</label>
    <input
      type="text"
      class="free-filter"

      v-model="freeTextFilter"
      placeholder="Free text filter eg. 'No more than 4 beds'..."
    />
  </div>

  <!-- Show the range inputs only when the toggle is OFF -->
  <div v-if="!useFreeTextFilter" class="ranges">
    <div class="bedrooms-range">
      <label for="bedrooms">Beds:</label>
      <input
        type="range"
        id="bedrooms"
        v-model="filterBeds"
        min="1"
        max="10"
      />
      <span>{{ filterBeds }}</span>
    </div>
    <div class="rooms-range">
      <label for="rooms">Rooms:</label>
      <input
        type="range"
        id="rooms"
        v-model="filterRooms"
        min="1"
        max="10"
      />
      <span>{{ filterRooms }}</span>
    </div>
  </div>
</div>

<div class="toggle-container">
  <label for="toggleFilter">Free text:</label>
  <input type="checkbox" id="toggleFilter" v-model="useFreeTextFilter" />
</div>


  
</div>
    <div v-if="listings.length<1" ><h1>No Apartments</h1></div>
    <div v-else="listings.length>0" class="grid" :class="{ 'grid-disabled': loading }">
      
     
      
      <div   v-for="listing in listings" :key="listing.id" class="listing">
        
        <img :src="listing.images?.picture_url" alt="Listing image">
        <h2>{{ listing.name }}</h2>
        <p v-if="!showMore[listing.id]">{{ shortDescription(listing.description) }}</p>
        <p v-else>{{ listing.description }}</p>
        <button @click="toggleShowMore(listing.id)">{{ showMore[listing.id] ? 'Read Less' : 'Read More' }}</button>
        <p><b>City</b>: {{ listing.address.market }}</p>
        <p><b>Rooms</b>: {{ listing.bedrooms }}</p>
        <p><b>Price</b>: ${{ listing.price }}</p>
        <p><b>Beds</b>: {{ listing.beds }}</p>
        <p><b>People</b>: {{ listing.accommodates }}</p>
        <p><b>Rating</b>: {{listing.review_scores.review_scores_rating }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import RangeSlider from 'vue-range-slider';

export default {
  data() {
    return {
      searchQuery: '',
      listings: [],
      filterBeds: '',
      filterRooms: '',
      filterPeople: '',
      loading: false,
      showMore: {},
      filterMaxPrice: 10000,
      useFreeTextFilter: false,
      freeTextFilter: '',
    }
  },
  mounted() {
    this.fetchListings();
  },
  methods: {
    async fetchListings() {
      try {
        this.loading = true;
        const params = {
          search: this.searchQuery,
          beds: this.filterBeds,
          rooms: this.filterRooms,
          people: this.filterPeople,
          // maxPrice: this.filterMaxPrice,
        };

        if (this.useFreeTextFilter) {
          this.filterBeds = '';
          this.filterRooms = '';
          this.filterPeople = '';
      params.freeTextFilter = this.freeTextFilter;
    }
        /*
          TODO: REPLACE WITH YOURS
          <ENDPOINT_APP_SERVICES> is the endpoint of your app services
        */
        const response = await axios.get(
          'https://us-east-1.aws.data.mongodb-api.com/app/application-0-dlfks/endpoint/search',
          { params }
        );
        this.loading = false;
        this.listings = response.data;

        // Initialize showMore for each listing
        this.listings.forEach(listing => {
          this.showMore[listing.id] = false;
        });
      } catch (error) {
        console.error(error);
      }
    },
    shortDescription(description) {
      if (description.length > 100) {
        return description.substring(0, 100) + '...';
      } else {
        return description;
      }
    },
    toggleFreeTextFilter() {
    this.useFreeTextFilter = !this.useFreeTextFilter;
  },
    toggleShowMore(id) {
      this.showMore[id] = !this.showMore[id];
    },
  },
}
</script>


<style scoped>
.search-input, .search-button {
  margin: 10px;
  
}

.search-area {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  gap: 10px;
}
.search-text{
  flex-direction: row;
  width: 100%;
}

.search-input {
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #ddd;
  width: 70%;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  padding: 10px;
}

.listing {
  border: 1px solid #ddd;
  padding: 10px;
  border-radius: 8px;
  overflow: hidden;
}

.listing img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 8px;
}

.grid-disabled {
  animation: opacityLoop 4s infinite;
  /* Adjust the blur radius as needed */
}

@keyframes opacityLoop {
  0%, 100% {
    opacity: 0.5;
    backdrop-filter: blur(50px); 
  }
  50% {
    opacity: 1;
    backdrop-filter: blur(50px); 
  }
}

.filters {
  display: flex;

  width: 100%;
  gap: 10px;
}

.free-filter{
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #ddd;
  width: 500px
}
</style>