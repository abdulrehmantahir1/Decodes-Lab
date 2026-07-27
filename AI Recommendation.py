"""
AI Recommendation System - Content-Based Filtering
Simple recommendation engine based on user preferences
"""

class RecommendationSystem:
    def __init__(self):
        # Sample dataset of items with their features
        self.items = {
            'movies': [
                {'id': 1, 'title': 'Inception', 'genre': 'Sci-Fi', 'rating': 8.8, 'director': 'Nolan'},
                {'id': 2, 'title': 'The Dark Knight', 'genre': 'Action', 'rating': 9.0, 'director': 'Nolan'},
                {'id': 3, 'title': 'Interstellar', 'genre': 'Sci-Fi', 'rating': 8.6, 'director': 'Nolan'},
                {'id': 4, 'title': 'The Godfather', 'genre': 'Drama', 'rating': 9.2, 'director': 'Coppola'},
                {'id': 5, 'title': 'Pulp Fiction', 'genre': 'Crime', 'rating': 8.9, 'director': 'Tarantino'},
                {'id': 6, 'title': 'The Shawshank Redemption', 'genre': 'Drama', 'rating': 9.3, 'director': 'Darabont'},
                {'id': 7, 'title': 'Avengers: Endgame', 'genre': 'Action', 'rating': 8.4, 'director': 'Russo'},
                {'id': 8, 'title': 'The Matrix', 'genre': 'Sci-Fi', 'rating': 8.7, 'director': 'Wachowski'},
                {'id': 9, 'title': 'Goodfellas', 'genre': 'Crime', 'rating': 8.7, 'director': 'Scorsese'},
                {'id': 10, 'title': 'The Social Network', 'genre': 'Drama', 'rating': 7.7, 'director': 'Fincher'}
            ],
            'books': [
                {'id': 1, 'title': 'The Alchemist', 'genre': 'Fiction', 'author': 'Coelho', 'rating': 4.5},
                {'id': 2, 'title': '1984', 'genre': 'Dystopian', 'author': 'Orwell', 'rating': 4.8},
                {'id': 3, 'title': 'To Kill a Mockingbird', 'genre': 'Fiction', 'author': 'Lee', 'rating': 4.9},
                {'id': 4, 'title': 'The Great Gatsby', 'genre': 'Fiction', 'author': 'Fitzgerald', 'rating': 4.4},
                {'id': 5, 'title': 'Harry Potter', 'genre': 'Fantasy', 'author': 'Rowling', 'rating': 4.7}
            ],
            'products': [
                {'id': 1, 'name': 'Laptop', 'category': 'Electronics', 'price': 999, 'brand': 'Dell'},
                {'id': 2, 'name': 'Smartphone', 'category': 'Electronics', 'price': 799, 'brand': 'Apple'},
                {'id': 3, 'name': 'Headphones', 'category': 'Electronics', 'price': 199, 'brand': 'Sony'},
                {'id': 4, 'name': 'Book: Python Programming', 'category': 'Books', 'price': 39, 'brand': 'O\'Reilly'},
                {'id': 5, 'name': 'Gaming Console', 'category': 'Electronics', 'price': 499, 'brand': 'Sony'}
            ]
        }
        
        # User preferences storage
        self.user_preferences = {}
    
    def get_user_preferences(self):
        """Get user preferences through interactive input"""
        print("\n" + "="*50)
        print("🎯 AI RECOMMENDATION SYSTEM")
        print("="*50)
        
        # Get user's name
        name = input("\nEnter your name: ").strip()
        
        # Get category preference
        print("\n📂 Available Categories:")
        categories = list(self.items.keys())
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat.capitalize()}")
        
        while True:
            try:
                choice = int(input("\nSelect category (1-3): "))
                if 1 <= choice <= 3:
                    category = categories[choice-1]
                    break
                else:
                    print("Please select a valid option (1-3)")
            except ValueError:
                print("Please enter a number")
        
        # Get genre/preference
        print(f"\n🎬 Available {category.capitalize()} Genres:")
        genres = set()
        for item in self.items[category]:
            if 'genre' in item:
                genres.add(item['genre'])
            elif 'category' in item:
                genres.add(item['category'])
        
        for i, genre in enumerate(sorted(genres), 1):
            print(f"{i}. {genre}")
        
        while True:
            try:
                choice = int(input("\nSelect your preferred genre: "))
                if 1 <= choice <= len(genres):
                    selected_genre = sorted(genres)[choice-1]
                    break
                else:
                    print(f"Please select a number between 1 and {len(genres)}")
            except ValueError:
                print("Please enter a number")
        
        # Get rating preference
        print("\n⭐ Rating Preference:")
        print("1. Any rating")
        print("2. 4.0 and above")
        print("3. 4.5 and above")
        
        while True:
            try:
                choice = int(input("Select rating preference (1-3): "))
                if 1 <= choice <= 3:
                    rating_filter = {1: 0, 2: 4.0, 3: 4.5}[choice]
                    break
                else:
                    print("Please select a valid option (1-3)")
            except ValueError:
                print("Please enter a number")
        
        # Store preferences
        self.user_preferences = {
            'name': name,
            'category': category,
            'genre': selected_genre,
            'min_rating': rating_filter
        }
        
        return self.user_preferences
    
    def calculate_similarity(self, item, preferences):
        """Calculate similarity score between item and user preferences"""
        score = 0
        matches = []
        
        # Check genre match
        item_genre = item.get('genre') or item.get('category', '')
        if item_genre.lower() == preferences['genre'].lower():
            score += 50
            matches.append(f"Genre: {preferences['genre']}")
        
        # Check rating
        item_rating = item.get('rating', 0)
        if item_rating >= preferences['min_rating']:
            score += item_rating * 5
            matches.append(f"Rating: {item_rating}★")
        
        # Bonus for high ratings
        if item_rating >= 9.0:
            score += 20
            matches.append("Top Rated!")
        
        return score, matches
    
    def get_recommendations(self, preferences, top_n=5):
        """Get top N recommendations based on user preferences"""
        category = preferences['category']
        items = self.items[category]
        
        recommendations = []
        for item in items:
            score, matches = self.calculate_similarity(item, preferences)
            recommendations.append({
                'item': item,
                'score': score,
                'matches': matches
            })
        
        # Sort by score (descending)
        recommendations.sort(key=lambda x: x['score'], reverse=True)
        
        return recommendations[:top_n]
    
    def display_recommendations(self, recommendations, preferences):
        """Display recommendations in a formatted way"""
        print("\n" + "="*50)
        print(f"📊 RECOMMENDATIONS FOR {preferences['name'].upper()}")
        print("="*50)
        print(f"Category: {preferences['category'].capitalize()}")
        print(f"Preferred Genre: {preferences['genre']}")
        print(f"Minimum Rating: {preferences['min_rating']}★")
        print("-"*50)
        
        if not recommendations or recommendations[0]['score'] == 0:
            print("\n😅 No matching items found. Try adjusting your preferences!")
            return
        
        for i, rec in enumerate(recommendations, 1):
            item = rec['item']
            score = rec['score']
            matches = rec['matches']
            
            print(f"\n{i}. {item.get('title', item.get('name', 'Unknown'))}")
            print(f"   📍 Score: {score:.1f}%")
            
            # Display item details
            for key, value in item.items():
                if key not in ['id', 'title', 'name']:
                    print(f"   📌 {key.capitalize()}: {value}")
            
            # Display matching features
            if matches:
                print(f"   ✅ Matches: {', '.join(matches)}")
            
            # Rating stars
            if 'rating' in item:
                stars = '⭐' * int(item['rating'] / 2)
                print(f"   {stars} ({item['rating']}★)")
        
        print("\n" + "="*50)
    
    def run(self):
        """Main execution method"""
        print("\n🚀 Welcome to AI Recommendation System!")
        
        # Get user preferences
        preferences = self.get_user_preferences()
        
        # Get recommendations
        recommendations = self.get_recommendations(preferences)
        
        # Display recommendations
        self.display_recommendations(recommendations, preferences)
        
        # Option to refine search
        while True:
            print("\n🔄 Options:")
            print("1. Get new recommendations")
            print("2. Refine search")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                preferences = self.get_user_preferences()
                recommendations = self.get_recommendations(preferences)
                self.display_recommendations(recommendations, preferences)
            elif choice == '2':
                self.refine_search()
            elif choice == '3':
                print("\n👋 Thank you for using AI Recommendation System!")
                print("Goodbye!\n")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def refine_search(self):
        """Allow user to refine their search"""
        print("\n🔍 REFINE SEARCH")
        print("="*50)
        
        # Get current preferences
        if not self.user_preferences:
            print("Please set preferences first!")
            return
        
        print(f"Current preferences:")
        print(f"Category: {self.user_preferences['category']}")
        print(f"Genre: {self.user_preferences['genre']}")
        print(f"Min Rating: {self.user_preferences['min_rating']}")
        
        # Ask for refinements
        print("\nWhat would you like to refine?")
        print("1. Change genre")
        print("2. Change rating")
        print("3. Back to main menu")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            # Change genre
            genres = set()
            for item in self.items[self.user_preferences['category']]:
                if 'genre' in item:
                    genres.add(item['genre'])
                elif 'category' in item:
                    genres.add(item['category'])
            
            print("\nAvailable genres:")
            for i, genre in enumerate(sorted(genres), 1):
                print(f"{i}. {genre}")
            
            try:
                choice = int(input("\nSelect genre: "))
                if 1 <= choice <= len(genres):
                    self.user_preferences['genre'] = sorted(genres)[choice-1]
                    print(f"✅ Genre updated to: {self.user_preferences['genre']}")
            except (ValueError, IndexError):
                print("Invalid selection")
        
        elif choice == '2':
            # Change rating
            print("\nSelect rating preference:")
            print("1. Any rating")
            print("2. 4.0 and above")
            print("3. 4.5 and above")
            
            try:
                choice = int(input("Enter choice (1-3): "))
                if 1 <= choice <= 3:
                    self.user_preferences['min_rating'] = {1: 0, 2: 4.0, 3: 4.5}[choice]
                    print(f"✅ Rating preference updated to: {self.user_preferences['min_rating']}★")
            except ValueError:
                print("Invalid selection")
        
        # Get new recommendations with refined preferences
        recommendations = self.get_recommendations(self.user_preferences)
        self.display_recommendations(recommendations, self.user_preferences)


# ============================================
# VERSION 2: Collaborative Filtering (Advanced)
# ============================================

class CollaborativeFiltering:
    """
    Advanced recommendation using collaborative filtering
    """
    def __init__(self):
        # User-item ratings matrix
        self.user_ratings = {
            'user1': {'Inception': 5, 'Dark Knight': 4, 'Interstellar': 5, 'Matrix': 3},
            'user2': {'Inception': 3, 'Dark Knight': 5, 'Godfather': 5, 'Pulp Fiction': 4},
            'user3': {'Inception': 4, 'Interstellar': 4, 'Matrix': 5, 'Avengers': 4},
            'user4': {'Godfather': 5, 'Pulp Fiction': 5, 'Goodfellas': 4, 'Shawshank': 5},
            'user5': {'Dark Knight': 5, 'Avengers': 4, 'Matrix': 3, 'Inception': 4}
        }
        
        # Items list
        self.items = ['Inception', 'Dark Knight', 'Interstellar', 'Godfather', 
                     'Pulp Fiction', 'Shawshank', 'Avengers', 'Matrix', 
                     'Goodfellas', 'Social Network']
    
    def calculate_similarity(self, user1, user2):
        """Calculate Pearson similarity between two users"""
        # Get common items rated by both users
        common_items = set(self.user_ratings[user1].keys()) & set(self.user_ratings[user2].keys())
        
        if not common_items:
            return 0
        
        # Calculate Pearson correlation
        ratings1 = [self.user_ratings[user1][item] for item in common_items]
        ratings2 = [self.user_ratings[user2][item] for item in common_items]
        
        # Simple cosine similarity
        dot_product = sum(r1 * r2 for r1, r2 in zip(ratings1, ratings2))
        norm1 = sum(r1 ** 2 for r1 in ratings1) ** 0.5
        norm2 = sum(r2 ** 2 for r2 in ratings2) ** 0.5
        
        if norm1 == 0 or norm2 == 0:
            return 0
        
        return dot_product / (norm1 * norm2)
    
    def get_recommendations(self, target_user, n=5):
        """Get recommendations for target user"""
        if target_user not in self.user_ratings:
            print(f"User {target_user} not found!")
            return []
        
        # Calculate similarity with all users
        similarities = {}
        for user in self.user_ratings:
            if user != target_user:
                similarities[user] = self.calculate_similarity(target_user, user)
        
        # Sort users by similarity
        similar_users = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        
        # Get items the target user hasn't rated
        target_items = set(self.user_ratings[target_user].keys())
        all_items = set(self.items)
        unrated_items = all_items - target_items
        
        # Predict ratings for unrated items
        recommendations = []
        for item in unrated_items:
            weighted_sum = 0
            similarity_sum = 0
            
            for user, similarity in similar_users[:3]:  # Top 3 similar users
                if item in self.user_ratings[user]:
                    weighted_sum += similarity * self.user_ratings[user][item]
                    similarity_sum += abs(similarity)
            
            if similarity_sum > 0:
                predicted_rating = weighted_sum / similarity_sum
                recommendations.append((item, predicted_rating))
        
        # Sort by predicted rating
        recommendations.sort(key=lambda x: x[1], reverse=True)
        
        return recommendations[:n]


# ============================================
# VERSION 3: Hybrid Recommendation System
# ============================================

class HybridRecommender:
    """
    Combines content-based and collaborative filtering
    """
    def __init__(self):
        self.content_recommender = RecommendationSystem()
        self.collaborative_recommender = CollaborativeFiltering()
    
    def hybrid_recommendation(self, user_preferences, target_user, n=5):
        """Combine recommendations from both systems"""
        # Get content-based recommendations
        content_recs = self.content_recommender.get_recommendations(user_preferences, n)
        
        # Get collaborative recommendations
        collab_recs = self.collaborative_recommender.get_recommendations(target_user, n)
        
        # Combine results (hybrid approach)
        combined = []
        for rec in content_recs:
            combined.append({
                'item': rec['item'],
                'source': 'content',
                'score': rec['score']
            })
        
        for item, rating in collab_recs:
            combined.append({
                'item': {'title': item, 'rating': rating, 'genre': 'Unknown'},
                'source': 'collaborative',
                'score': rating * 10
            })
        
        # Sort by score
        combined.sort(key=lambda x: x['score'], reverse=True)
        
        return combined[:n]


# ============================================
# MAIN EXECUTION
# ============================================

def main():
    """Main entry point for the recommendation system"""
    print("\n" + "="*60)
    print("🌟 AI RECOMMENDATION SYSTEM - COMPLETE PROJECT")
    print("="*60)
    
    print("\nSelect Recommendation Engine:")
    print("1. Content-Based Filtering (Simple)")
    print("2. Collaborative Filtering (Advanced)")
    print("3. Hybrid Recommender (Best)")
    print("4. Compare All Methods")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-4): "))
            if 1 <= choice <= 4:
                break
            print("Please select a valid option (1-4)")
        except ValueError:
            print("Please enter a number")
    
    if choice == 1:
        # Content-Based
        recommender = RecommendationSystem()
        recommender.run()
    
    elif choice == 2:
        # Collaborative Filtering
        print("\n🔍 Collaborative Filtering Engine")
        print("="*50)
        
        cf = CollaborativeFiltering()
        
        print("\nAvailable users:", list(cf.user_ratings.keys()))
        target_user = input("\nEnter username (user1-user5): ").strip()
        
        recommendations = cf.get_recommendations(target_user)
        
        print(f"\n📊 Recommendations for {target_user}:")
        print("-"*50)
        for i, (item, rating) in enumerate(recommendations, 1):
            print(f"{i}. {item} - Predicted Rating: {rating:.2f}★")
    
    elif choice == 3:
        # Hybrid Recommender
        print("\n🔀 Hybrid Recommendation Engine")
        print("="*50)
        
        hybrid = HybridRecommender()
        
        # Get user preferences
        preferences = hybrid.content_recommender.get_user_preferences()
        
        print("\nAvailable users:", list(hybrid.collaborative_recommender.user_ratings.keys()))
        target_user = input("Enter username for collaborative filtering (user1-user5): ").strip()
        
        recommendations = hybrid.hybrid_recommendation(preferences, target_user)
        
        print(f"\n📊 Hybrid Recommendations for {target_user}:")
        print("-"*50)
        for i, rec in enumerate(recommendations, 1):
            item = rec['item']
            title = item.get('title', item.get('name', 'Unknown'))
            print(f"{i}. {title}")
            print(f"   Source: {rec['source']}")
            print(f"   Score: {rec['score']:.1f}")
    
    elif choice == 4:
        # Compare all methods
        print("\n📊 Comparing All Recommendation Methods")
        print("="*50)
        
        # Content-based
        print("\n1️⃣ Content-Based Recommendations:")
        content = RecommendationSystem()
        prefs = content.get_user_preferences()
        content_recs = content.get_recommendations(prefs, 3)
        for i, rec in enumerate(content_recs, 1):
            item = rec['item']
            title = item.get('title', item.get('name', 'Unknown'))
            print(f"   {i}. {title} (Score: {rec['score']:.1f})")
        
        # Collaborative
        print("\n2️⃣ Collaborative Filtering:")
        cf = CollaborativeFiltering()
        print("   Available users:", list(cf.user_ratings.keys()))
        target_user = input("   Enter username: ").strip()
        collab_recs = cf.get_recommendations(target_user, 3)
        for i, (item, rating) in enumerate(collab_recs, 1):
            print(f"   {i}. {item} (Predicted Rating: {rating:.2f})")
        
        # Hybrid
        print("\n3️⃣ Hybrid Recommendations:")
        hybrid = HybridRecommender()
        # Use same preferences from content-based
        hybrid_recs = hybrid.hybrid_recommendation(prefs, target_user, 3)
        for i, rec in enumerate(hybrid_recs, 1):
            item = rec['item']
            title = item.get('title', item.get('name', 'Unknown'))
            print(f"   {i}. {title} (Score: {rec['score']:.1f})")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for using AI Recommendation System!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try again.")