<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  
  <xsl:template match="/">
    <html>
      <body>
        <!-- Thế Vinh -->
        <h2>Đơn hàng và tổng sau giảm giá</h2>
        <table border="1">
          <tr><th>Mã đơn</th><th>Tên KH</th><th>Tổng sau giảm giá</th></tr>
          <xsl:for-each select="root/orders/order">
            <tr>
              <td><xsl:value-of select="@id" /></td>
              <td><xsl:value-of select="customer_name" /></td>
              <td><xsl:value-of select="format-number(total_amount - (total_amount * discount div 100), '#.00')" /></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h2>Số lượng sách theo thể loại</h2>
        <table border="1">
          <tr><th>Thể loại</th><th>Số lượng sách</th></tr>
          <xsl:for-each select="root/genres/genre">
            <tr>
              <td><xsl:value-of select="genre_name" /></td>
              <td><xsl:value-of select="count(/root/genre_details/genre_detail[@genre_id=current()/@id])" /></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <!-- Thành Trí -->
        
        <!-- Quốc Việt -->
        
      </body>
    </html>
  </xsl:template>
  
</xsl:stylesheet>
