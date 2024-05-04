import streamlit as st
def main():
    st.title("Course videos")

    st.subheader("Videos")
    img=[['/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp'],['/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp'],['/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp'],['/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp']]
    Link=[['https://www.youtube.com/watch?v=CBYhVcO4WgI','https://www.youtube.com/watch?v=CBYhVcO4WgI','https://www.youtube.com/watch?v=CBYhVcO4WgI','https://www.youtube.com/watch?v=CBYhVcO4WgI'],['https://www.youtube.com/watch?v=CBYhVcO4WgI','https://www.youtube.com/watch?v=CBYhVcO4WgI','https://www.youtube.com/watch?v=CBYhVcO4WgI','https://www.youtube.com/watch?v=CBYhVcO4WgI'],['https://www.youtube.com/watch?v=CBYhVcO4WgI','https://www.youtube.com/watch?v=CBYhVcO4WgI','https://www.youtube.com/watch?v=CBYhVcO4WgI','https://www.youtube.com/watch?v=CBYhVcO4WgI'],['https://www.youtube.com/watch?v=CBYhVcO4WgI','https://www.youtube.com/watch?v=CBYhVcO4WgI','https://www.youtube.com/watch?v=CBYhVcO4WgI','https://www.youtube.com/watch?v=CBYhVcO4WgI']]
    
    c=1
    j=0
    for f in range(3):
            col1, col2,col3,col4=st.columns(4)
            with col1:
                st.image(img[f][0], caption=f"Link: {Link[f][0]}",  width=120)
                st.page_link("https://www.youtube.com/watch?v=CBYhVcO4WgI",label="To watch")
            with col2:
                st.image(img[f][1], caption=f"Link: {Link[f][1]}",  width=120)
                st.page_link("https://www.youtube.com/watch?v=CBYhVcO4WgI",label="To watch")
                
            with col3:
                st.image(img[f][2], caption=f"Link: {Link[f][2]}",  width=120)
                st.page_link("https://www.youtube.com/watch?v=CBYhVcO4WgI",label="To watch")
            with col4:
                st.image(img[f][3], caption=f"Link: {Link[f][3]}",  width=120) 
                st.page_link("https://www.youtube.com/watch?v=CBYhVcO4WgI",label="To watch")
                    



if __name__ == "__main__":
    main()