<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <body>
        <!-- Thế Vinh -->
        <h2>Đơn hàng và tổng sau giảm giá</h2>
        <table border="1">
          <tr>
            <th>Mã đơn</th>
            <th>Tên KH</th>
            <th>Tổng sau giảm giá</th>
          </tr>
          <xsl:for-each select="root/orders/order">
            <tr>
              <td>
                <xsl:value-of select="@id" />
              </td>
              <td>
                <xsl:value-of select="customer_name" />
              </td>
              <td>
                <xsl:value-of
                  select="format-number(total_amount - (total_amount * discount div 100), '#.00')" />
              </td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>Số lượng sách theo thể loại</h2>
        <table border="1">
          <tr>
            <th>Thể loại</th>
            <th>Số lượng sách</th>
          </tr>
          <xsl:for-each select="root/genres/genre">
            <tr>
              <td>
                <xsl:value-of select="genre_name" />
              </td>
              <td>
                <xsl:value-of
                  select="count(/root/genre_details/genre_detail[@genre_id=current()/@id])" />
              </td>
            </tr>
          </xsl:for-each>
        </table>

        <!-- Thành Trí -->
        <h2>Sách thể loại tình cảm</h2>
        <table border="1">
          <tr>
            <th>Mã sách</th>
            <th>Tiêu đề</th>
            <th>Giá</th>
          </tr>
          <xsl:for-each select="root/genre_details/genre_detail[@genre_id='G001']">
            <xsl:variable name="book_id" select="@book_id" />
            <xsl:for-each select="/root/books/book[@id=$book_id]">
              <tr>
                <td>
                  <xsl:value-of select="@id" />
                </td>
                <td>
                  <xsl:value-of select="title" />
                </td>
                <td>
                  <xsl:value-of select="format-number(price, '#.00')" />
                </td>
              </tr>
            </xsl:for-each>
          </xsl:for-each>
        </table>

        <h2>Sách của tác giả Lê Nhật Thiên</h2>
        <table border="1">
          <tr>
            <th>Mã sách</th>
            <th>Tiêu đề</th>
            <th>Giá</th>
          </tr>
          <xsl:for-each select="root/books/book">
            <xsl:variable name="this_books" select="." />
            <xsl:variable name="book_id" select="@id" />
            <xsl:for-each select="/root/author_details/author_detail[@book_id=$book_id and @author_id='AU006']">
              <tr>
                <td>
                  <xsl:value-of select="$this_books/@id" />
                </td>
                <td>
                  <xsl:value-of select="$this_books/title" />
                </td>
                <td>
                  <xsl:value-of select="format-number($this_books/price, '#.00')" />
                </td>
              </tr>
            </xsl:for-each>
          </xsl:for-each>
        </table>
        <!-- Quốc Việt -->
        <h2>Tổng đơn hàng và chi phí của người dùng</h2>
        <table border="1">
          <tr>
            <th>Mã người dùng</th>
            <th>Tên</th>
            <th>Số đơn hàng</th>
            <th>Tổng tiền đã chi</th>
          </tr>
          <xsl:for-each select="root/users/user">
            <xsl:variable name="user_id" select="@id"/>
            <xsl:variable name="orders" select="/root/orders/order[@customer_id=$user_id]"/>
            <tr>
              <td><xsl:value-of select="@id"/></td>
              <td><xsl:value-of select="username"/></td>
              <td><xsl:value-of select="count($orders)"/></td>
              <td>
                <xsl:choose>
                  <xsl:when test="count($orders) &gt; 0">
                    <xsl:value-of select="format-number(sum($orders/total_amount), '#.00')"/>
                  </xsl:when>
                  <xsl:otherwise>0</xsl:otherwise>
                </xsl:choose>
              </td>
            </tr>
          </xsl:for-each>
        </table>
        <h2>Tổng review và điểm trung bình của người dùng</h2>
        <table border="1">
          <tr>
            <th>Mã người dùng</th>
            <th>Tên</th>
            <th>Số review</th>
            <th>Điểm trung bình</th>
          </tr>
          <xsl:for-each select="root/users/user">
            <xsl:variable name="user_id" select="@id"/>
            <xsl:variable name="reviews" select="/root/reviews/review[@user_id=$user_id]"/>
            <tr>
              <td><xsl:value-of select="@id"/></td>
              <td><xsl:value-of select="username"/></td>
              <td><xsl:value-of select="count($reviews)"/></td>
              <td>
                <xsl:choose>
                  <xsl:when test="count($reviews) &gt; 0">
                    <xsl:value-of select="format-number(sum($reviews/rating) div count($reviews), '#.00')"/>
                  </xsl:when>
                  <xsl:otherwise>0</xsl:otherwise>
                </xsl:choose>
              </td>
            </tr>
          </xsl:for-each>
        </table>

      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>