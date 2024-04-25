import streamlit as st
def main():
    st.title("STARTUP PAGE")

    st.subheader("Startups")
    img=[['/workspaces/task-streamlit/image/flinto.jpg', '/workspaces/task-streamlit/image/netmeds.jpg','/workspaces/task-streamlit/image/sulekha.png'],['/workspaces/task-streamlit/image/flinto.jpg', '/workspaces/task-streamlit/image/netmeds.jpg','/workspaces/task-streamlit/image/sulekha.png'],['/workspaces/task-streamlit/image/flinto.jpg', '/workspaces/task-streamlit/image/netmeds.jpg','/workspaces/task-streamlit/image/sulekha.png']]
    Date=[['About: Flintobox is an India-based company that produces STEAM-based educational activity boxes for children. Based on a new theme every month, Flintobox designs resources for Early Child Development.', 'Netmeds Healthcare Limited operates as an online pharmacy. The Company offers eyewear, fitness, personal care, prescribed medicines, and health products. Netmeds Healthcare serves customers in India.', 'Sulekha is a matchmaking platform identifies relevant businesses based on the service type, location preference, and other factors. Once the match is found, we send the customers information to the matched businesses. The businesses can contact the customers directly and convert them to customers.'],['Flintobox is an India-based company that produces STEAM-based educational activity boxes for children. Based on a new theme every month, Flintobox designs resources for Early Child Development. ', 'Netmeds Healthcare Limited operates as an online pharmacy. The Company offers eyewear, fitness, personal care, prescribed medicines, and health products. Netmeds Healthcare serves customers in India.', 'Sulekha is a matchmaking platform identifies relevant businesses based on the service type, location preference, and other factors. Once the match is found, we send the customers information to the matched businesses. The businesses can contact the customers directly and convert them to customers.'],['Flintobox is an India-based company that produces STEAM-based educational activity boxes for children. Based on a new theme every month, Flintobox designs resources for Early Child Development. ', 'Netmeds Healthcare Limited operates as an online pharmacy. The Company offers eyewear, fitness, personal care, prescribed medicines, and health products. Netmeds Healthcare serves customers in India.', 'Sulekha is a matchmaking platform identifies relevant businesses based on the service type, location preference, and other factors. Once the match is found, we send the customers information to the matched businesses. The businesses can contact the customers directly and convert them to customers.']]
    j=0
    for f in range(3):
            col1, col2,col3=st.columns(3)
            with col1:
                st.image(img[f][0], caption=f"Date: {Date[f][0]}", width=200)
                st.page_link("https://flintobox.com/",label="To connect")
            with col2:
                st.image(img[f][1], caption=f"Date: {Date[f][1]}", width=200)
                st.pagelink("https://www.netmeds.com/",label="To connect")
            with col3:
                st.image(img[f][2], caption=f"Date: {Date[f][2]}", width=200) 
                st.page_link("https://www.sulekha.com/",label="To connect")
    



if __name__ == "__main__":
    main()

